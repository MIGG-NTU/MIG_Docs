Cluster
=======

These two names are the same cluster ``GEKKO``. You can use any of them, because the IP address for those two names are the same.

- ``gekko.earthobservatory.sg``
- ``gekko.hpc.ntu.edu.sg``

GEKKO is EOS's cluster.

- For EOS user, it is free.
- For other NTU user, it will be charged.

GEKKO also has 8 GPU. If you would like to use GPU, please contact Edwin Tan Seng Tat (EdwinTan@ntu.edu.sg) for more help.


Account & Password
------------------

- Account: NTU account (e.g., ``jiayuanyao``)
- Password: NTU password (e.g., ``123456``)
- Log in: ``ssh jiayuanyao@gekko.earthobservatory.sg``


Prof. Tong Ping's Projects
---------------------------

PBS-Pro requires a project group to function. Prof Tong Ping has two project groups: ``spms_tongping`` and ``eos_tongping``.

- The account `spms_tongping` will be charge at 4 cents per core hour.
- The account ``eos_tongping`` will not be charge, as EOS had already paid for the resources. It can be used for running collaboration jobs with EOS.


Manual
------

General guide
+++++++++++++

- `NTU-HPC Website <https://entuedu.sharepoint.com/teams/ntuhpcusersgroup2>`_: you can find a lot of manuals here.
- `NTU-HPC Yammer Users’ Group Site <https://www.yammer.com/e.ntu.edu.sg/#/threads/inGroup?type=in_group&feedId=15849979904&view=all>`_: you can also download from the App Store / Google Play / Microsoft Office Site. Do log in with your NTU-ID. The Yammer Group is called “NTU HPC Users' Group".
- `User Guide <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/User%20Guide/Forms/AllItems.aspx?RootFolder=%2Fsites%2Fhpc%2FUser%20Guide%2Fgekko%2Dcluster&FolderCTID=0x012000B75E77F6895B184182BB95924F3CE8F3&View=%7BFDF6D033%2DDC8E%2D459B%2DAE2E%2DEE8C1DD67F06%7D>`_
- When you get a account, you should test if you can run a task. Sometimes your account may not be set up, and you cannot submit a task (an error *qsub: Unauthorized Request* may appear). Please use the following example using GPU to test.

Using CPU
+++++++++

- Please copy the script file from ``/usr/local/templates``, e.g., ``mpi.pbs`` or ``matlab.pbs``, to your working folder. Then you edit the file and change the below:

    - ``#PBS -P eee_userid`` change to ``#PBS -P eos_tongping``
    - ``#PBS -q q32`` change to ``#PBS -q q32_eos``
    - ``q32`` allows max of 512 cores per user. ``q32_eos`` is specially for eos user where you can run 1024 cores. Now, it seems that there are between those two queues no difference at all.
- To submit a task, run the script, e.g., ``qsub mpi.pbs -v inputfile=your_binary_script``.

Using GPU
+++++++++

- The GPU resources consist of 2 GPU servers with 8 GPU cards each. You can access it through the queue ``gpu8``.
- The template GPU submission script is available at ``/usr/local/templates/gpu/gpu.pbs``.
- You can change the variable of *ngpus* in the submission scripts to request for the number of GPU cards you required. The system will allocate the GPU cards to you when the job runs.
- For each GPU card requests, 4 CPU cores will be allocated automatically by the system. Thus the variable in the *ncpus* will be overwritten by the system.
- Command line

    - run ``qsub -l select=1:ncpus=32:ngpus=1 -P eos_tongping -q gpu8 -I`` to require GPU in the command line
    - run ``nvidia-smi`` to see details about the GPU
    - run ``module load cuda/10.1`` to load cuda/10.1. You can put it in bashrc

Use Python
++++++++++

Edwin has installed ``Anaconda`` on Gekko, and he suggested us use Anaconda to create virtual environment where we can run python packages with better version control. Version control usually is important for python.

.. code-block:: bash

    # 1. Create the virtual env
    # myvirtual: just a name of your virtual environment
    # The following are essential packages you want to install (Python, Obspy, etc.)
    $ conda create -n myvirtual obspy=1.2.1 python=3

    # 2. Activate virtual environment
    # The virtual environment is permanently saved in your home folder
    $ conda activate myvirtual

    # 3. In your virtual environment, you have the sudo user permission.
    # For example, install more packages using the normal conda or pip commands.
    $ conda install matplotlib
    $ pip install matplotlib

    # 4. Do anything in you virtual environment
    $ git clone https://github.com/core-man/seismic-data.git


Using Scratch Space
+++++++++++++++++++

**An initial notice sent to Jiayuan Yao:**

If you are hoping to speed up your work especially if you have reading/writing lots of data (I/O intensive),  you may want to use ``/scratch/username``. The scratch space is a fast scratch space several time faster than home directory. It was meant to speed up computing run (nearly **3 times faster**). So you will recover back your time.. But you have to clear off the data manually after the run as the scratch space is very expensive and limited.

**An notice posted in Yammer on Dec. 14 2020**

- `original note <https://www.yammer.com/e.ntu.edu.sg/#/threads/show?threadId=989272424267776>`__

NVMe Scratch Space has been increased from **50TB** to **150TB**. Speed up your work by using this fast scratch space!

We have upgraded the NVMe Scratch so that you can have the lowest latency and highest performance especially when your Read/Write to the disk is high.

Every users should have a scratch space called ``/scratch/youruserid``. You can copy the specific folder (not your entire home directory please) that you are running there and submit your jobs via ``qsub``. **Upon completion of the job, copy the essential files or folder back to your home directory**.

Do note that the scratch directory is not a home directory to store data permanently. It is a super-fast read/write space

If you are not sure how to use it drop me an private email via yammer.


Quota
+++++

- Default Disk Quota (200GB) per user. For additional space, please see the `website <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Charges>`_
- For EOS user, default disk quota is 500GB. If you need more, such as 10TB, please drop a mail to Edwin Tan Seng Tat (EdwinTan@ntu.edu.sg).
- Each node has a memory of 384GB.


Other Notes
+++++++++++

- Submission Scripts: log in the cluster, and copy from ``/usr/local/templates``.
- A new queue @Gekko called ``budget_night`` which is 50% cheaper. The catch is that the job will only run from 6 pm onwards and it has 12 hours wall-time limits only. But there is no restriction in the number of cores you can use. For more information do get it from Yammer (NTU HPC Users' Group) or NTU-HPC website.
- `Computing and storage charges <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Charges>`_
- Software and Hardware Inventories
    - `Hardware Inventories <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Hardware%20Configuration>`_
    - `Software Inventories <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Software%20Inventory>`_
- `Purchase Form <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Forms/Forms/AllItems.aspx>`_
- If you have any query, feel free to drop a mail to Edwin Tan Seng Tat (EdwinTan@ntu.edu.sg) at EOS, or hpcsupport@ntu.edu.sg

