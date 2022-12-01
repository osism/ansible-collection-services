This ansible role install Haveged.
Haveged is a random number generator.

**Role Variables**

.. zuul:rolevar:: rng_service_name
   :default: haveged

Service name of haveged.

.. zuul:rolevar:: rng_package_name
   :default: haveged

Package name for installing haveged.
