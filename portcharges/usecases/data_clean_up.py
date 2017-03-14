import pprint

from portcharges.domain import PortCharge


class _RangeGenerator:

    def __init__(self, range_count):
        self._range_count = range_count

    def generate(self, port_charges):
        min_value = int(min([
            port_charge.value for port_charge in port_charges]))
        max_value = int(
            max([port_charge.value for port_charge in port_charges]))
        range_step = int((max_value - min_value) / self._range_count)
        ranges = self._generate_ranges(min_value, max_value, range_step)
        return self._group_data(ranges, port_charges)

    def _generate_ranges(self, min_value, max_value, range_step):
        ranges = list(zip(
            range(min_value, max_value, range_step),
            range(
                min_value + range_step,
                max_value + range_step,
                range_step,
            ),
        ))
        return [
            (range[0]+ranges.index(range), range[1]+ranges.index(range))
            for range in ranges
        ]

    def _group_data(self, ranges, port_charges):
        grouped = {}
        for port_charge in port_charges:
            range = self._select_range(ranges, port_charge)
            self._add_range(grouped, range, port_charge)
        return grouped

    def _select_range(self, ranges, port_charge):
        for range in ranges:
            if port_charge.value >= range[0] and port_charge.value <= range[1]:
                return range

    def _add_range(self, grouped, range, port_charge):
        try:
            grouped[range].append(port_charge.id)
        except KeyError:
            grouped[range] = [port_charge.id]


class DataCleanUpUseCase:

    def __init__(self, data_finder, data_updater, stats_finder):
        self._data_finder = data_finder
        self._range_generator = _RangeGenerator(range_count=5)
        self._data_updater = data_updater
        self._stats_finder = stats_finder

    def clean(self):
        for port_charges in self._get_port_charges():
            distribution = self._range_generator.generate(port_charges)
            outliers = self._select_least_populated(distribution)
            self._data_updater.update(outliers)
        return pprint.pformat(list(self._stats_finder.find()))

    def _get_port_charges(self):
        for charges_by_country in list(self._data_finder.find()):
            yield list(self._deserialize(charges_by_country['port_charges']))

    def _deserialize(self, port_charges):
        for port_charge in port_charges:
            yield PortCharge(
                id=port_charge['_id'],
                country=port_charge['country'],
                city=port_charge['city'],
                supplier_id=port_charge['supplier_id'],
                value=port_charge['value'],
            )

    def _select_least_populated(self, distribution):
        min_count = min(len(values) for values in distribution.values())
        outliers = []
        for range in distribution:
            if len(distribution[range]) == min_count:
                outliers.extend(distribution[range])
        return outliers
