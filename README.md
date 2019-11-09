# demo-python

A demo project for python.

## Reference

* Environment
    * [Conda](https://docs.conda.io/en/latest/miniconda.html)
    * [pyenv](https://github.com/pyenv/pyenv)
    * [pyenv-installer](https://github.com/pyenv/pyenv-installer)
* Style
    * [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html)
    * [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* Modules
    * [Flask](http://flask.palletsprojects.com/en/1.1.x/)
    * [flask-swagger](https://pypi.org/project/flask-swagger/)
    * [click](https://click.palletsprojects.com/en/7.x/)
    * [requests](https://requests.kennethreitz.org/en/master/)
    * [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)
    * [Writing the Setup Script](https://docs.python.org/3/distutils/setupscript.html)
* Logging
    * [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
* Trace
    * [Trace or track Python statement execution](https://docs.python.org/3.0/library/trace.html)
* Monitoring
    * [prometheus/client_python](https://github.com/prometheus/client_python)
    * [getsentry/sentry-python](https://github.com/getsentry/sentry-python)
* Package
    * [Writing the Setup Script](https://docs.python.org/3/distutils/setupscript.html)
    * [Creating a Source Distribution](https://docs.python.org/3/distutils/sourcedist.html)
    * [Making a PyPI-friendly README](https://packaging.python.org/guides/making-a-pypi-friendly-readme/)
    * [Including files in source distributions with MANIFEST.in](https://packaging.python.org/guides/using-manifest-in/)
* Mirrors
    * [mirrors.aliyun.com](http://mirrors.aliyun.com/pypi/simple)
    * [pypi.douban.com](http://pypi.douban.com/simple)
    * [pypi.v2ex.com](http://pypi.v2ex.com/simple)

> Version management: conda or pyenv (slow in mainland china) 

## conda

```
wget -c -P /tmp/ https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

bash /tmp/Miniconda3-latest-MacOSX-x86_64.sh

conda info -e

conda create -n demo

conda activate demo python=3.7

which python 

python --version

conda deactivate 
```

## pyenv

### Install pyenv

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

. ~/.bash_profile
```

### Download package before install by pyenv

> China only

```
mirrors="https://mirror.bjtu.edu.cn"
pyver="3.7.3" # 3.7.3, 2.7.17

# Download python before install by pyenv
mkdir -p ~/.pyenv/cache/
wget -c -P ~/.pyenv/cache/ ${mirrors}/python/${pyver}/Python-${pyver}.tar.xz
pyenv install ${pyver}
pyenv local ${pyver}

pyenv versions
```

