# Python 101


## Virtualenvs

Virtualenvs (or virtual environments) are essentially in Python development by keeping dependency libraries isolated from each other.

An example of this is when, say, we have two ongoing projects, but each needs a different version of a particular library.

If dependencies were kept at the system level, we'd likely be only able to install one version of the library at any one time. With `virtualenv`, we're able to keep the dependencies of each project isolated from each other.

### Requirements

Before proceeding, ensure you have the package `virtualenv`

If you have Python already installed,

	$ pip3 install virtualenv

This should install `virtualenv` on your system

### Setting up

Assuming our project sits at `~/myawesomeproject`.

First, we want to select where our dependencies are going to live, let's say `~/myawesomeproject/venv`.

_While it's not necessary to have the `virtualenv` directory sit within your project folder, it's often convenient to have it nearby for easy reference._

Then we're going to instantiate the virtual environment

	$ cd ~/myawesomeproject
	$ virtualenv -p python3 ./venv
	Running virtualenv with interpreter /usr/bin/python3
	Using base prefix '/usr'
	New python executable in /home/ruiwen/myawesomeproject/pytimate/venv/bin/python3
	Also creating executable in /home/ruiwen/myawesomeproject/pytimate/venv/bin/python
	Installing setuptools, pkg_resources, pip, wheel...done.

This should create the directory `~/myawesomeproject/venv` with  the following contents

	$ ls ./venv/
	bin  include  lib  pip-selfcheck.json  share

`~/myawesomeproject/venv` is your virtual environment, in which all your project dependencies will live, isolated from the other projects on your host system.

### Activating / Deactivating

Once the virtualenv is set up, we'll need to activate it.

	$ . ./venv/bin/activate
	(venv) $

Activating the virtualenv calls a bunch of scripts that modify the current shell's environment (and its prompt). The effect of this is to enable your current shell to use an isolated copy of Python that knows how to locate its own set of libraries.

Run the commands below before and after activating your virtualenv, and see the difference in the paths output.

Before activation

	$ which python
	/usr/bin/python
	$ which pip
	/usr/bin/pip
	$ . ./venv/bin/activate

After activation

	(venv) $ which python
	/home/ruiwen/myawesomeproject/venv/bin/python
	(venv) $ which pip
	/home/ruiwen/myawesomeproject/venv/bin/pip

Once your virtualenv is activated, the `python` binary that you're running should no longer be the system level binary at, eg. `/usr/bin/python`, but should be the one that's in your virtualenv, at, eg. `~/myawesomeproject/venv/bin/python`. When activated, the virtualenv scripts actively modify the `PATH` environment variable in order to get your shell to use the `python` binary in the virtualenv first, before the system-level `python` binary.

	$ echo $PATH
	/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
	$ . ./venv/bin/activate
	(venv) $ echo $PATH
	/home/ruiwen/myawesomeproject/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

Since the path to our virtualenv (`/home/ruiwen/myawesomeproject/venv/bin/`) now appears first in our `$PATH`, our shell will pick up the binary there first, instead of from `/usr/bin/`.

Once we're done working on our project, we'd like to reset our `$PATH` back to what it once was, so we `deactivate` the virtualenv

	(venv) $ deactivate
	$ echo $PATH
	/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

And now we're out of our virtualenv!


