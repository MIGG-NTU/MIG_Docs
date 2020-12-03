Git & GitHub
============

MIG uses `Git <https://github.com/git/git>`__ and `Github <https://github.com/>`__ to manage softwares and documents. All the members cannot push revisions to the main branch of all the public repositories. For private branches, all the memebers **MUST NOT** push revisions to the main branch either. Instead, all the revisions must be reviewed and approved using **Pull Request**.


Git
---

`Git <https://git-scm.com/>`__ is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals. Please refer to the following references for details.

- `git 简易指南 <https://www.bootcss.com/p/git-guide/index.html>`_
- `Git教程 (廖雪峰) <https://www.liaoxuefeng.com/wiki/896043488029600>`_
- `Pro Git (中文版) <https://git-scm.com/book/zh/v2>`_
- `Git Cheat Sheet <https://www.git-tower.com/blog/git-cheat-sheet/>`_


A list of some commonly-used git commands:

.. code-block:: bash

    # clone a remote repository to your local computer
    $ git clone git@github.com:username/repository_name.git

    # add the revisions in one file or all the files to Index
    $ git add filename
    $ git add --all
    # commit the revisions to HEAD
    $ git commit -m "revise filename"

    # push the revisions to remote repository
    $ git push origin master

    # create and go to a new branch
    $ git checkout -b bug_x
    # go to master branch
    $ git checkout master

    # delete a fully merged branch
    $ git branch -d bug_x
    # delete a branch
    $ git branch -D bug_x

    # fetch and merge the revisions in remote repository
    $ git pull
    # merge revisions at branch bug_x to current branch
    $ git merge bug_x


GitHub
------

`Github <https://github.com/>`__  provides hosting for software development and version control using ``Git``.

- `Documentation <https://docs.github.com/cn/free-pro-team@latest/github>`__
- `Understanding the GitHub flow <https://guides.github.com/introduction/flow/>`__


A list of some commonly-used commands in GitHub command-line tools:

- `hub <https://hub.github.com/>`_: an extension to command-line git that helps you do everyday GitHub tasks without ever leaving the terminal.

.. code-block:: bash

    # fast-forward all local branches to match the latest state on the remote
    $ hub sync


- `GitHub CLI <https://cli.github.com/>`_: take GitHub to the command line

.. code-block:: bash

    # create a pull request and request reviews by core-man, HouseJaay, Shucheng-Wu, tianjueli
    $ gh pr create --reviewer core-man,HouseJaay,Shucheng-Wu,tianjueli


A Workflow Example
------------------

We use the repository, `MIG_Docs <https://github.com/MIGG-NTU/MIG_Docs>`__, as an example to show how we should revise and update a GitHub repository on which at least two authors are working.

`Branch protection rules <https://docs.github.com/cn/free-pro-team@latest/github/administering-a-repository/configuring-protected-branches>`__ is used to protect the **master** branch, along with two activated rules:

- Require pull request reviews before merging: 1 reviewer
- Include administrators


We use the following `pull request merging method <https://docs.github.com/cn/free-pro-team@latest/github/administering-a-repository/configuring-pull-request-merges>`__:

- Allow squash merging
- Automatically delete head branches


Preparation
+++++++++++

1. clone the remote repository if it is the first time:

.. code-block:: console

    $ git clone git@github.com:MIGG-NTU/MIG_Docs.git


Maintainment
++++++++++++

1. Update the local branches from remote since others may revise the remote branches

.. code-block:: console

    # frist way: use hub
    $ hub sync
    # second way: use git pull
    $ git checkout main
    $ git pull

2. Create a feature branch (e.g., ``feature_x``) in which we update and commit the revisions

.. code-block:: console

    $ git checkout -b feature_X

3. Do some revisions on the feature_X branch, and check them by building the repository locally at the same time. You have to install `Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`__ and `Read the Docs Sphinx Theme <https://github.com/readthedocs/sphinx_rtd_theme>`__ to build the website locally.

.. code-block:: console

    $ make html                            # build the website locally
    $ google-chrome build/html/index.html& # check the website in a website browser

4. Commit the revisions. You can do the revisions and commit them for many times.

.. code-block:: console

    $ git status
    $ git add --all
    $ git status
    $ git commit -m "leave a revise message here"

5. When you do the revisions locally, the remote ``main`` branch may be updated. So, we have to always synchronize with the remote ``main`` branch.

.. code-block:: console

   # first way
   # synchronize with remote main branch using hub
   $ hub sync
   # rebase the feature branch to be based on the latest main branch
   $ git rebase main

   # second way
   # synchronize with remote main branch using git pull
   $ git checkout main
   $ git pull
   # checkout to feature branch and rebase it to be based on the latest main branch
   $ git checkout feature_X
   $ git rebase master


6. When you revise the content, there could be many commits. Some commits may be not so important. You can squash some commits into one or several commits so that the revisions are clear and easy to manage.

.. code-block:: console

   $ git rebase -i main


7. When you think the revisions are okay, create a pull request and request at least 1 reviewer:

.. code-block:: console

    $ gh pr create -r core-man,HouseJaay,Shucheng-Wu,tianjueli

8. Review/Approval/Merge on GitHub

   - The reviewers review the commit by commentting and/or approving it online.
   - If everything is fine, the author can go to the GitHub website to merge the commit.
   - If there are conflicts, the author needs to resolve them locally and push to remote again.
   - When commits are merged, the feature_X branch will be automatically deleted in Github.

9. When commits are merged, we have to update the local branches:

.. code-block:: console

    $ hub sync                 # update the local branches since the remote master has been updated
    $ git checkout main        # checkout to main branch
    $ git branch -D feature_X  # delete local feature branch


In summary, we first add revisions in a local feature branch, and submit a pull request. If it is approved and merged to the remote master branch, we then have to update the local main branch with the remote one. At last, the local feature has to be deleted.
