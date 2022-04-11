Fugaku
========

:contributors: |Xu Mijian|
:last updating date: 2022-04-04


Get access
------------

Preparation 
++++++++++++++

- **Passphrase for Supercomputer Fugaku**: this is a ``.pdf`` file involving passphrase code, which used to access the certificate file. This file can be downloaded with a link in an e-mail with the subject of "Your passphrase for the supercomputer Fugaku".

    .. note::
        This link requires a verification with password of ``hpci-id#verification code``. The ``hpci-id`` and ``verification code`` can be found in an e-mail with the subject of "News of registered HPCI-ID".


- **Certificate file**: this file with filename of ``uxxxxx.p12`` can be downloaded via an e-mail with the subject of "Notification of client certificate for the Supercomputer Fugaku".

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


Login into Fugaku
++++++++++++++++++

The address of login node is ``login.fugaku.r-ccs.riken.jp``. We recommand ssh clients in different platform:

- Windows

  - `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__
  - `MobaXterm <https://mobaxterm.mobatek.net/>`__

  .. note::

    The Fugaku requires key pair (public key / private key) to login. See `Startup Guide <https://www.hpci-office.jp/fugaku/user-info/e_index.html>`__ in detail. To login via ``PuTTY``, please use `PuTTYgen <https://www.puttygen.com/>`__ to convert the private key (``id_rsa``) to the ``.ppk`` format.   

- MacOS and Linux

  Login directly from the terminal. The private key should be save to ``~/.ssh/id_rsa``. The permissions should be set to ``600``

  ::
    
    chmod 600 ~/.ssh/id_rsa

Disk Resources
----------------

Quota limit of the home area
++++++++++++++++++++++++++++++

As the e-mail of "【富岳運用情報】 ホーム領域の容量制限について / 【Fugaku Operation Info】 About the quota limit of the home area", the home area limits have been set to 20 GiB and 6000 i-node (number of files). Please use ``accountd_home`` to check data usage, and ``accountd_home -i`` to check i-node usage.

::

    $ accountd_home
    COLLECTDATE : 2022/04/11 16:10:02    unit[GiB] 
    USER : u10305
    *--------------------------------------------------[USER]------------------------------------------------------*
    USER            VOLUME                       LIMIT             USAGE         AVAILABLE           FILES  USE_RATE
    u10305          vol0301                         20                 1                19           1,850      2.2%

    $ accountd_home -i
    COLLECTDATE : 2022/04/11 16:11:18     
    USER : u10305
    *--------------------------------------------------[USER]------------------------------------------------------*
    USER            VOLUME                      ILIMIT             IUSED             IFREE                  USE_RATE
    u10305          vol0301                      6,000             1,850             4,150                     30.8%


Quota limit of the volume area
+++++++++++++++++++++++++++++++

The `User Guide <https://www.fugaku.r-ccs.riken.jp/doc_root/en/user_guides/use_latest/UsageRules/index.html#disk>`__ list 5 types of disk area: home area, data area, share area, tmpfs area, and 2ndfs area. We have been assigned with a group id of ``hp220155``. All users under this group share the data area, 2ndfs area and share area. 

- data area: ``/vol0003/mdt1/data/hp220155``
- share area: ``/vol0003/mdt1/share/hp220155``
- 2ndfs area: ``/2ndfs/hp220155``

.. note::

    All users can access under ``/share/groupname/``. Do not put any data here. The share directory can be referenced from the above path only from the login node.

We can list the data usage and i-node usage as:

::

    $ accountd_volume 
    COLLECTDATE : 2022/04/11 16:26:00    unit[GiB] 
    USER : u10305
    ......
    *--------------------------------------------------[GROUP]-----------------------------------------------------*
    GROUP           FILESYSTEM                   LIMIT             USAGE         AVAILABLE           FILES  USE_RATE
    hp220155        /vol0001                     5,120                 9             5,111         112,938      0.2%
    hp220155        /vol0003                     5,120                 3             5,117          12,495      0.0%
    hp220155        /vol0004                       ---                 1               ---               8       ---
    hp220155        /vol0005                       ---                 1               ---               8       ---
    hp220155        /vol0006                       ---                 1               ---              10       ---
    *--------------------------------------------------[USER]------------------------------------------------------*
    USER            FILESYSTEM                   LIMIT             USAGE         AVAILABLE           FILES  USE_RATE
    u10305          /vol0001                 unlimited                 9         unlimited         117,052       ---
    u10305          /vol0003                 unlimited                 3         unlimited          14,334       ---
    u10305          /vol0004                 unlimited                 0         unlimited               0       ---
    u10305          /vol0005                 unlimited                 0         unlimited               0       ---
    u10305          /vol0006                 unlimited                 0         unlimited               0       ---

    $ accountd_volume -i
    COLLECTDATE : 2022/04/11 16:27:38     
    USER : u10305
    ......
    *--------------------------------------------------[GROUP]-----------------------------------------------------*
    GROUP           FILESYSTEM                  ILIMIT             IUSED             IFREE                  USE_RATE
    hp220155        /vol0001                 1,500,000           112,938         1,387,062                      7.5%
    hp220155        /vol0003                 1,500,000            12,495         1,487,505                      0.8%
    hp220155        /vol0004                       ---                 8               ---                       ---
    hp220155        /vol0005                       ---                 8               ---                       ---
    hp220155        /vol0006                       ---                10               ---                       ---
    *--------------------------------------------------[USER]------------------------------------------------------*
    USER            FILESYSTEM                  ILIMIT             IUSED             IFREE                  USE_RATE
    u10305          /vol0001                 unlimited           117,052         unlimited                       ---
    u10305          /vol0003                 unlimited            14,334         unlimited                       ---
    u10305          /vol0004                 unlimited                 0         unlimited                       ---
    u10305          /vol0005                 unlimited                 0         unlimited                       ---
    u10305          /vol0006                 unlimited                 0         unlimited                       ---


Using compilers
--------------------
Fugaku's login node and compute node use `x86_64` and `Arm` architectures respectively. Therefore, programs compiled on the login node cannot be run on the compute node.

Compilation on the compute node
+++++++++++++++++++++++++++++++++
We need to create a interactive job to login into compute node

::

    pjsub --interact -L "elapse=1:00:00" -g hp220155 --no-check-directory

Fujitsu compiler, LLVM, and GNU compiler are available. See `Compilers that generate binaries for compute nodes <https://www.fugaku.r-ccs.riken.jp/doc_root/en/user_guides/lang_latest/CompileforCN/index.html#compilerforcn>`__ in detail.

Compilation on the compute node
+++++++++++++++++++++++++++++++++

Intel compiler and mkl library can be loaded via

::

    module load mpi/2021.2.0 compiler/2021.2.0 mkl/2021.2.0
    source /opt/intel/oneapi/setvars.sh

Jobs management
--------------------
