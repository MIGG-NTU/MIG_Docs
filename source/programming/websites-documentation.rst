Websites & Documentation
========================

:contributors: |Yao Jiayuan|
:last updating date: 2021-05-22

----

`Hugo <https://gohugo.io/>`__ is used to build the static websites, e.g.,
Prof. Ping Tong's `homepage <https://personal.ntu.edu.sg/tongping/>`__.
We use the hugo module, `wowchemy <https://github.com/wowchemy/wowchemy-hugo-modules>`__.

`Sphinx <https://www.sphinx-doc.org/en/master/>`__ is used to build the documentation,e.g.,
`MIG_Docs <https://migg-ntu.github.io/MIG_Docs/>`__.
We use the `Read the Docs Sphinx <https://github.com/readthedocs/sphinx_rtd_theme>`__ theme.

`Jekyll <https://jekyllrb.com/>`__ is used to build MIGG-NTU's
`Github User Page <https://migg-ntu.github.io/>`__,
using the `modernist <https://github.com/pages-themes/modernist>`__ theme.

All the websites and documentation are hosted at `GitHub <https://github.com/MIGG-NTU>`__
using `GitHub Pages <https://pages.github.com/>`__.
`GitHub Actions <https://docs.github.com/cn/free-pro-team@latest/actions>`__
or `Travis CI <https://travis-ci.com/>`__ is used to build and deploy the websites and documentation.


MIG Website Settings
--------------------

========================================================================= ============== ======================== ================ =====================
Websites                                                                  Generators     Themes                   Hostings         Building & Deployment
========================================================================= ============== ======================== ================ =====================
`MIG homepage <https://personal.ntu.edu.sg/tongping/>`__                  ``Hugo``       ``Wowchemy Module``      ``GitHub Pages`` ``Travis CI``
`MIG_Docs <https://migg-ntu.github.io/MIG_Docs/>`__                       ``Sphinx``     ``Read the Docs Sphinx`` ``GitHub Pages`` ``GitHub Actions``
`SeisTomo_Tutorials <https://migg-ntu.github.io/SeisTomo_Tutorials/>`__   ``Sphinx``     ``Read the Docs Sphinx`` ``GitHub Pages`` ``GitHub Actions``
`geosciences_Myanmar <https://migg-ntu.github.io/geosciences_Myanmar/>`__ ``Sphinx``     ``Read the Docs Sphinx`` ``GitHub Pages`` ``GitHub Actions``
`MIGG-NTU.github.io <https://github.com/MIGG-NTU/MIGG-NTU.github.io>`__   ``Jekyll``     ``modernist``            ``GitHub Pages`` ``GitHub``
========================================================================= ============== ======================== ================ =====================

Hugo
----

`Hugo <https://gohugo.io/>`__ is the world’s fastest framework for building static websites:

- `Install <https://gohugo.io/getting-started/installing/>`__  | `Releases <https://github.com/gohugoio/hugo/releases>`__
- `Documentation <https://gohugo.io/documentation/>`__ | `中文文档 <https://www.gohugo.org/>`__

**Themes:**

`Wowchemy <https://wowchemy.com/>`__ (`GitHub <https://github.com/wowchemy/wowchemy-hugo-modules>`__)
is a popular website builder for Hugo. It is now a `Hugo Module <https://gohugo.io/hugo-modules/>`__
and previously was a Hugo Theme called ``hugo-academic``.
Some `Wowchemy Templates <https://wowchemy.com/templates/>`__ are available, e.g., ``Academic Starter`` (previous ``academic-kickstart``).

You can edit the website on the local PC using Wowchemy along with some `prerequisites <https://wowchemy.com/docs/install-locally/#prerequisites>`__.
Please refer to `Wowchemy Documentation <https://wowchemy.com/docs/>`__ for more details.

Hugo provides a lot of useful `Themes <https://themes.gohugo.io/>`__ which can be also used to build our websites.

**Website examples:**

- `uOttawa Geophysics <https://www.uogeophysics.com/>`__ | `GitHub <https://github.com/paudetseis/academic-kickstart>`__
- `GMT 中文社区 <https://gmt-china.org/>`__ | `GitHub <https://github.com/gmt-china/gmt-china.org>`__
- `Dongdong Tian's homepage <https://me.seisman.info/>`__ | `GitHub <https://github.com/seisman/academic-homepage>`__
- `Jiayuan Yao's homepage <https://core-man.github.io/academic-homepage/>`__ | `GitHub <https://github.com/core-man/academic-homepage>`__

**Tutorials:**

We can refer to some parts of those tutorials, because the settings in our websites are a little different.

- `借助 Hugo 和 Academic 主题在 github <https://leidawt.github.io/post/%E5%80%9F%E5%8A%A9hugo%E5%92%8Cacademic%E4%B8%BB%E9%A2%98%E5%9C%A8github/>`__
- `academic 主题 <https://skyao.io/learning-hugo/docs/theme/academic.html>`__
- `Academic 实现 Github Page 个人博客 <https://szthanatos.github.io/post/academic/academic_in_practice/>`__

Sphnix
------

`Sphnix <https://www.sphinx-doc.org/>`__  is a tool that makes it easy to create intelligent and beautiful documentation.

- `Install <https://www.sphinx-doc.org/en/master/usage/installation.html>`__
- `Documentation <https://www.sphinx-doc.org/en/master/contents.html>`__: `Using Sphinx <https://www.sphinx-doc.org/en/master/usage/index.html>`__

**Themes:**

- `HTML Theming <https://www.sphinx-doc.org/en/master/usage/theming.html>`__
- `Read the Docs Sphinx <https://github.com/readthedocs/sphinx_rtd_theme>`__ provided by `Read the Docs <https://readthedocs.org/>`__

**Documentation examples:**

- `GMT Documentation <https://docs.generic-mapping-tools.org/latest/>`__ | `GitHub <https://github.com/GenericMappingTools/gmt>`__
- `GMT 中文手册 <https://docs.gmt-china.org/latest/>`__ | `GitHub <https://github.com/gmt-china/GMT_docs>`__
- `SAC 参考手册 <https://seisman.github.io/SAC_Docs_zh/>`__ | `GitHub <https://github.com/seisman/SAC_Docs_zh>`__

**Tutorials:**

- `How to document with Sphinx tutorial <https://www.youtube.com/watch?v=_xDgNKc6-AI&list=PLE72UCmIe7T9HewaqCUhKqiMK3LxYStjy>`__
- `Sampledoc <https://matplotlib.org/sampledoc/>`__: a very nice tutorial on how to create a customized documentation using Sphinx written by the matplotlib developers
- `使用单个仓库配置 GitHub Pages + Sphinx <https://natescarlet.github.io/2019/05/11/%E4%BD%BF%E7%94%A8%E5%8D%95%E4%B8%AA%E4%BB%93%E5%BA%93%E9%85%8D%E7%BD%AE-github-pages-sphinx/>`__
- `如何用Sphinx、GitHub、ReadtheDocs 搭建写书环境 <https://wtf.readthedocs.io/en/latest/index.html>`__

GitHub Pages
------------

`GitHub Pages <https://pages.github.com/>`__ is a static site hosting service that takes ``HTML``, ``CSS``, and ``JavaScript`` files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website.

- `Documentation <https://docs.github.com/cn/free-pro-team@latest/github/working-with-github-pages>`__
- `如何把 Hugo 生成的博客托管在 GitHub Pages <https://www.gohugo.org/doc/tutorials/github-pages-blog/>`__
- `发布到Github Pages <https://einverne.github.io/gitbook-tutorial/publish/gitpages.html>`__
- `解决Github Pages 和 Github .md 文件图片不显示 <https://www.cnblogs.com/Java-Starter/p/11087031.html>`__

Github Actions
--------------

`GitHub Actions <https://docs.github.com/cn/free-pro-team@latest/actions>`__ makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub. Make code reviews, branch management, and issue triaging work the way you want.

**Tutorials:**

- `Quick Start <https://docs.github.com/cn/free-pro-team@latest/actions/quickstart>`__
- `GitHub Actions 入门教程 <http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html>`__
- `GitHub Actions 自动部署 <https://segmentfault.com/a/1190000021815477>`__
- `GitHub Action 一键部署 <https://didiheng.com/front/2019-12-11.html#github-action%E9%85%8D%E7%BD%AE>`__

Travis CI
---------

`Travis CI <https://travis-ci.com/>`__ is a continuous integration (CI) platform used to build and test code changes, provide immediate feedback on the success of the change, and manage deployments and notifications. Please refer to the `Documentation <https://docs.travis-ci.com/>`__ for more details.

**Tutorials:**

- `Travis CI Tutorial <https://docs.travis-ci.com/user/tutorial/>`__
- `持续集成服务 Travis CI 教程 <http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html>`__
- `使用 Travis CI 自动部署 Hugo 博客 <https://mogeko.me/2018/028/>`__
