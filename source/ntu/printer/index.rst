Printers
========

:contributors: |Yao Jiayuan|,
               |Wu Shucheng|
:last updating date: 2021-05-22

----

NTU use *MPS* printer queue. There is a black-white printer in MAS-04-07.
Besides, we can use color printers in the Heads of Division office (SPMS-PAP-02-01) near the elevator in the second floor in SPMS.
There are also two color printers in the fifth floor of MAS. But, only a PI can open the door of the room with printers in the fifth floor.
We can check the task status via http://mps/mydoc after we submit a printing task.

Install Printer Driver
-----------------------

- `Install on Macintosh <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/master/source/resources-ntu/printer/NTUMPS-MAC.pdf>`__
- `Install on Windows <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/master/source/resources-ntu/printer/NTUMPS-WIN.pdf>`__

.. note::

   For macOS Big Sur (11.0.1 and later) user, the HP driver provided by Apple corrently does not support the system version,
   please go to `HP website <https://support.hp.com/us-en/drivers/printers>`__ to download the newer driver via the **HP Easy Start**.
    
   To use the HP Easy Start, you need to know the printer model (for MAS-04-07, the model is LaserJet Pro M404dn),
   and the printer IP address. You can get this info on the printer by printing out the **Network Configuration Page**,
   the current IP is ``10.97.164.29`` but it may change in the future.

MPS printer queue
-----------------

For macOS, it is the same as the above manual, except the following parts:

- URL is ``smb://172.21.4.94/PRINT`` or ``smb://mps.ntu.edu.sg/PRINT``
- The software is ``HP Color LaserJet flow MFP M880``

For Windows, it is the same as the above manual, except the following parts:

- Run ``\\172.21.4.94\PRINT` or `\\MPS/PRINT``


MPS printer at MAS-04-07
------------------------

For macOS, it is the same as the above manual, except the following parts:

- URL is ``smb://mps.ntu.edu.sg/SPMS-MAS-04-07-M01``.
- The software is ``HP LaserJet Pro M404dn``. If there is no such a sofware,
  you can choose ``HP LaserJet 400 M401``, ``HP LaserJet Pro M201-M202``, or ``HP LaserJet Pro M701``.
  It seems that the first one work well. The third one seems to have some problems with duplex printing. If you have a better choice, please tell us.
- `manual <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/master/source/resources-ntu/printer/MAS-04-07-MAC.pdf>`__

For Windows, it is the same as the above manual, except the following parts:

- Run ``\\MPS.NTU.EDU.SG``.
- If prompted for Network User Name (domain/username) and Password, key in your NTU Credentials.
- In the list, look for SPMS-MAS-04-07-M01, right click and select connet.
- Printer Model: HP Uniserval Printing PCL 6 (v6.6.0)
- `manual <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/master/source/resources-ntu/printer/MAS-04-07-WIN.jpeg>`__

Notes
-----

If you use MAC, please go to ``Printers & Scanners`` -> ``Options & Supplies`` -> ``Options``, and click ``Duplex Unit``.

If the printer at MAS-04-07 cannot work and does not show "MFD mode", please check if paper is stuck in the bottom or the
middle of the printer. If it shows the "MFG mode", just print the power button slighntly and the screen will show "Ready".
