Clusters
========

:contributors: |Yao Jiayuan|
:last updating date: 2021-05-22

----

We usually use a cluter called GEKKO. Its address is **gekko.earthobservatory.sg** or **gekko.hpc.ntu.edu.sg**,
both of which are the same. GEKKO is owned by EOS, while it is now maintained by NTU HPC.
It is free for EOS users, while it will be charged for other users at NTU.

Account
-------

We need to apply for an account before we can use GEKKO. Please ask Tong Ping for help.
If the NTU network account is jiayuanyao, then we could use ``ssh`` to log in Gekko::

    $ ssh jiayuanyao@gekko.earthobservatory.sg
    
It is recommended to use VS Code to log in Gekko and work on codes and files.
Please refer to a `VS Code tutorial <https://seismo-learn.org/seismology101/computer/editor/#vs-code>`__.

.. note::

   When you get a account, you should test if you can run a task.
   Sometimes your account may not be set up, and you cannot submit a task
   (an error ``qsub: Unauthorized Request`` may appear).
   Please use the following example to test.

Project Group
-------------

PBS-Pro requires a project group to function. Prof Tong Ping has two project groups:

- **spms_tongping**: 4 cents per core hour
- **eos_tongping**: free and no charge since EOS has already paid for the resources.
  It can be used for running collaboration jobs with EOS

Manual
------

General guide
+++++++++++++

- `NTU-HPC <https://entuedu.sharepoint.com/teams/ntuhpcusersgroup2>`_: you can find a lot of manuals here.
  Please read :file:`Quick User Guide for Gekko` to learn some basic usage of GEKKO.
- `NTU-HPC Yammer Users’ Group Site <https://www.yammer.com/e.ntu.edu.sg/#/threads/inGroup?type=in_group&feedId=15849979904&view=all>`_:
  you can also download from the App Store/Google Play/Microsoft Office Site.
  Do log in with your NTU-ID. The Yammer Group is called "NTU HPC Users' Group"
- `GEKKO User Guide <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/User%20Guide/Forms/AllItems.aspx?RootFolder=%2Fsites%2Fhpc%2FUser%20Guide%2Fgekko%2Dcluster&FolderCTID=0x012000B75E77F6895B184182BB95924F3CE8F3&View=%7BFDF6D033%2DDC8E%2D459B%2DAE2E%2DEE8C1DD67F06%7D>`__

Using CPU
+++++++++

Please copy the script file from :file:`/usr/local/templates` (e.g., :file:`mpi.pbs` or :file:`matlab.pbs``)
to your working folder. Then you could edit it based on your task, e.g.,:

- ``#PBS -P eee_userid`` -->> ``#PBS -P eos_tongping``
- ``#PBS -q q32`` -->> ``#PBS -q q32_eos``

.. note::

   Please see `Queue Information Pricing <https://entuedu.sharepoint.com/teams/ntuhpcusersgroup2/SitePages/Queue-Information-and-Pricing.aspx>`__.

   ``q32`` allows max of 512 cores per user.
   ``q32_eos`` is specially for eos user where you can run 1024 cores.
   However, it seems that there are between those two queues no difference at all now.

   A new queue @Gekko called ``budget_night`` which is 50% cheaper.
   The catch is that the job will only run from 6 pm onwards and it has 12 hours wall-time limits only.
   But there is no restriction in the number of cores you can use.
   For more information do get it from Yammer (NTU HPC Users' Group) or NTU-HPC website.

Run the script to submit a task::

    qsub mpi.pbs -v inputfile=your_binary_script

Using GPU
+++++++++

GEKKO also has 8 GPU. The GPU resources consist of 2 GPU servers with 8 GPU cards each.
You can access it through the queue ``gpu8``. The template GPU submission script is available at :file:`/usr/local/templates/gpu/gpu.pbs`.
You can change the variable of *ngpus* in the submission scripts to request for the number of GPU cards you required.
The system will allocate the GPU cards to you when the job runs.
For each GPU card requests, 4 CPU cores will be allocated automatically by the system.
Thus the variable in the *ncpus* will be overwritten by the system.

::

    # require GPU
    $ qsub -l select=1:ncpus=32:ngpus=1 -P eos_tongping -q gpu8 -I
      
    # check GPU details
    $ nvidia-smi
      
    # load cuda/10.1. You can write it in ~/.bashrc
    $ module load cuda/10.1

Use Python
++++++++++

Edwin has installed Anaconda on Gekko, and he suggested us use Anaconda to create virtual environment
where we can run python packages with better version control. Version control usually is important for python.
See `seismo-learn/software/anaconda <https://seismo-learn.org/software/anaconda/#id2>`__ for a brief tutorial.

::

    # 1. Create virtual environment (e.g., myvirtual)
    $ conda create --name myvirtual

    # 2. Activate virtual environment
    $ conda activate myvirtual

    # 3. Install packages in the virtual environment via either conda or pip
    $ conda install matplotlib
    $ pip install matplotlib

Using Scratch Space
+++++++++++++++++++

**An initial notice sent to Jiayuan Yao**

If you are hoping to speed up your work especially if you have reading/writing lots of data (I/O intensive),
you may want to use ``/scratch/username``. The scratch space is a fast scratch space several time faster than home directory.
It was meant to speed up computing run (nearly **3 times faster**).
So you will recover back your time. But you have to clear off the data manually after the run as the scratch space is very expensive and limited.

**An notice posted in Yammer on Dec. 14 2020** (`link <https://www.yammer.com/e.ntu.edu.sg/#/threads/show?threadId=989272424267776>`__)

NVMe Scratch Space has been increased from **50TB** to **150TB**. Speed up your work by using this fast scratch space!

We have upgraded the NVMe Scratch so that you can have the lowest latency and highest performance especially when your Read/Write to the disk is high.

Every users should have a scratch space called ``/scratch/youruserid``.
You can copy the specific folder (not your entire home directory please) that you are running there and submit your jobs via ``qsub``.
**Upon completion of the job, copy the essential files or folder back to your home directory**.

Do note that the scratch directory is not a home directory to store data permanently. It is a super-fast read/write space

If you are not sure how to use it drop me an private email via yammer.

Notes
+++++

``Module``::

    # check all options of module
    $ module

We could set up some packages in the setting file, e.g., :file:`~/.bashrc`::

    # Load intel
    module load intel/2018u3
    
    # Load MATLAB
    module load matlab/R2019b
    
    # Load CUDA
    module load cuda/10.1

Quota
+++++

Each node has a memory of 384 GB. Default disk quota is 500 GB for an EOS user.
If you need more (e.g., 10 TB), please drop a mail to Edwin Tan Seng Tat (EdwinTan@ntu.edu.sg).
Default disk quota is 200 GB for other user, and please see the `website <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Charges>`__ for additional space.

Software and Hardware Inventories:
`Hardware Inventories <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Hardware%20Configuration>`__ |
`Software Inventories <https://ts.ntu.edu.sg/sites/hpc/_layouts/15/start.aspx#/Software%20Inventory>`__

If you have any query, feel free to drop a mail to Edwin Tan Seng Tat (EdwinTan@ntu.edu.sg) at EOS, or hpcsupport@ntu.edu.sg
