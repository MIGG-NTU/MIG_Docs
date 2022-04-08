Fugaku
========

:contributors: |Xu Mijian|
:last updating date: 2022-04-04


Get access
------------

Preparation 
++++++++++++++

- **Passphrase for Supercomputer Fugaku**: this is a ``.pdf`` file involving passphrase code, which used to access the certificate file. This file can be downloaded with a link in an e-mail with subject of "Your passphrase for the supercomputer Fugaku".

    .. note::
        This link requires a verification with password of ``hpci-id#verification code``. The ``hpci-id`` and ``verification code`` can be found in an e-mail with subject of "News of registered HPCI-ID".


- **Certificate file**: this file with filename of ``uxxxxx.p12`` can be downloaded via an e-mail with subject of "Notification of client certificate for the Supercomputer Fugaku".

Install  client certificate
++++++++++++++++++++++++++++

MacOS and Windows
^^^^^^^^^^^^^^^^^^^^

A manual how to install the client certificate and how to
start an access to the Fugaku can be obtained from the
below open accessed link: https://www.hpci-office.jp/fugaku/user-info/e_index.html

Linux
^^^^^^^^^
``TODO``

Using compilers
--------------------

The Fugaku provide `Modules <https://modules.readthedocs.io/en/latest/index.html>`__ to manage packages. Available packages can be listed via

::

    module avail

Packages can be loaded via

::

    module load xxx

Arm compiler
+++++++++++++
``TODO``

Intel complier
+++++++++++++++
Intel compiler and mkl library can be loaded via

::

    module load mpi/2021.2.0 compiler/2021.2.0 mkl/2021.2.0
    source /opt/intel/oneapi/setvars.sh

Jobs management
--------------------
