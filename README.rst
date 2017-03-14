===========
portcharges
===========


Installing
==========

.. code-block:: bash

  pip install -e .

Saving data to db:

.. code-block:: bash

  python portcharges/main/save_charges_from_json.py portcharges/config/local.ini sample_data.json


Cleaning suspicious results and presenting the results:

.. code-block:: bash

  python portcharges/main/clean_up_data_and_return_results.py portcharges/config/local.ini