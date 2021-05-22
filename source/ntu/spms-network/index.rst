Network Configuration
=====================

:contributors: |Yao Jiayuan|
:last updating date: 2021-05-22

----

Network Segmentation
--------------------

An Email on 27 February 2020
+++++++++++++++++++++++++++++

To beef up network security and protect our NTU resources from intruders,
NTU will be implementing network segmentation on our wired network on ``2nd March`` at 6pm till 2am.
Please take note as any device connecting to NTU wired network after the implementation will require
a valid NTU authentication otherwise they will only be granted Internet access and no access to NTU internal resources.

**How does this affect you?**

Network segmentation breaks up the network into 4 different segments and you are allocated one
based on which domain you belong to in NTU. After the implementation, for users using a corporate device,
you do not need to do anything. For users using a personal device, you would be prompted to log in to
the network once and each time you change your password.

- **Segment 1**: For all NTU staff. Users in this segment has access to ALL NTU resources and the internet.
- **Segment 2**: For NTU students. Users in this segment has access to TEL resources, the schools’ server farm and the internet.
- **Segment 3**: For devices that are deemed safe but cannot be authenticated.
  Devices in this segment has access to NTU internal network and the internet.
  These devices have to be approved by the SPMS IT office or CITS and deemed safe before their MAC addresses can be allowed in this segment.
  Examples of such devices are CCTV, MPS printers and Apple TV.
- **Segment 4**: Devices that are not authenticated by an NTU account.
  Devices in this segment has access to the internet only.

An Email on 3 March 2020
+++++++++++++++++++++++++

Network segmentation has been successfully implemented on **all wired connections** last night.
Wireless connections are not affected.

For those who are using computers joined to NTU’s domain,
the transition would be seamless and the network would place you in the staff segment.
Your IP address will be ``10.85.XXX.XXX``.
if your computer is not in this segment, please perform a reboot of your computer.

For those who are using computers that are not joined to NTU’s domain,
some of you might still be in segment 4 (Internet Only) until a pop up appears for you to authenticate.
Computers in segment 4 will have IP address like ``10.101.XXX.XXX``.
If the pop up to authenticate does not appear, please follow the guides according to your computer’s operating system
`Linux <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/main/source/ntu/spms-network/Linux.pdf>`__
`macOS <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/main/source/ntu/spms-network/macOS.pdf>`__
`Windows <https://raw.githubusercontent.com/MIGG-NTU/MIG_Docs/main/source/ntu/spms-network/Windows.pdf>`__.
When the steps are completed, a pop up will appear asking for authentication.
Once authenticated, you can check your IP address again and you should be in segment 1 with IP address ``10.85.XXX.XXX``.

If you are still facing any issues, do log a case with ServiceNow first before dropping by the IT office.
The nice guys from NCS who did the implementation for us are seated outside the IT office and
they will be around from today till Thursday, 9am to 5pm to solve your issues.
You can log a case by clicking on the contact us button on ServiceNow which is located at the bottom right corner of the home page.

NTU wireless network
--------------------

`CITS <https://www.ntu.edu.sg/cits/Pages/index.aspx>`_ has upgraded NTU’s wireless network
to the latest version to remove the SMBv1.0 and TLS 1.0 protocols to address security vulnerabilities on 1st Apr 2020.
With this upgrade, MacBook users with old macOS ``Sierra 10.12.6`` and ``below`` will not be able to access the wireless network.
This is because the older macOS is not able to support EAP-TLS 1.2 and Apple’s KB
https://support.apple.com/en-sg/HT207828 indicates that only macOS ``High Sierra 10.13.6`` and ``later``
uses TLS 1.2 as the default for EAP-TLS negotiation.

We need to upgrade your MacBook macOS to the latest version and upload
the NTU wireless profile in order to use the wireless network.
The steps to upload the NTU wireless profile can be found
`here <https://www.ntu.edu.sg/cits/NTUwireless/Pages/Mac_OS_NTUSECURE.aspx>`__.

Access intranet via wired connection
------------------------------------
To access intranet via wired connection, need to config authentication method to be PEAP.
Here is a `document <https://www.virtualizationhowto.com/2018/12/configure-windows-10-for-802-1x-user-authentication/>`_.
