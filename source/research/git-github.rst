Git & GitHub
============

MIG uses `Git <https://github.com/git/git>`__ and `Github <https://github.com/>`__ to manage softwares and documents. All the members cannot push revisions to the main branch of all the public repositories. For private branches, all the memebers **MUST NOT** push revisions to the main branch either. Instead, all the revisions must be reviewed and approved using `Pull Request`.


Git
---

`Git <https://github.com/git/git>`__ is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals. Please refer to the following references for details.

- `git 简易指南 <https://www.bootcss.com/p/git-guide/index.html>`_
- `Git教程 (廖雪峰) <https://www.liaoxuefeng.com/wiki/896043488029600>`_
- `Pro Git (中文版) <https://git-scm.com/book/zh/v2>`_
- `Git Cheat Sheet <https://www.git-tower.com/blog/git-cheat-sheet/>`_


A list of some commonly-used git commands:

.. code-block:: bash

    # initialization of a new git repository
    git init
    # clone a remote repository to your local computer
    git clone git@github.com:username/repository_name.git

    # add the revisions to Index
    git add filename
    git add --all
    # commit the revisions to HEAD
    git commit -m "revise filename"

    # push the revisions to remote repository
    git push origin master

    # work on Branches
    # create and go to a new branch
    git checkout -b bug_x
    # go to master branch
    git checkout master
    # delete a fully merged branch
    git branch -d bug_x
    # delete a branch
    git branch -D bug_x

    # update and merge
    # fetch and merge the revisions in remote repository
    git pull
    # merge revisions at branch bug_x to current branch
    git merge bug_x


GitHub
------

`Github <https://github.com/>`__  provides hosting for software development and version control using `Git <https://github.com/git/git>`__. Please refer to `Github Docs <https://docs.github.com/en>`_ for details.


A list of some commonly-used commands in GitHub command-line tools:

- `hub <https://hub.github.com/>`_: an extension to command-line git that helps you do everyday GitHub tasks without ever leaving the terminal.

.. code-block:: bash

    # fast-forward all local branches to match the latest state on the remote
    hub sync


- `GitHub CLI <https://cli.github.com/>`_: take GitHub to the command line

.. code-block:: bash

    # create a pull request and request reviews by core-man, HouseJaay, Shucheng-Wu, tianjueli
    gh pr create --reviewer core-man,HouseJaay,Shucheng-Wu,tianjueli

