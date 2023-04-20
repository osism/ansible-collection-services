This ansible role install rng-tools.
rng-tools include the Daemon to use a Hardware TRNG random number generator.
The rngd daemon acts as a bridge between a Hardware TRNG.

**Role Variables**

.. zuul:rolevar:: rng_tools_service_name
   :default: rngd

Service name of rngd.

.. zuul:rolevar:: rng_tools_package_name
   :default: rng-tools

Package name for installing rng-tools.
