#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers."""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['54.236.30.33', '52.91.132.222']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not exists(archive_path):
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        remote_path = "/tmp/{}".format(archive_name)
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder_name))
        put(archive_path, remote_path)
        run("sudo tar -xzf {} -C /data/web_static/releases/{}/".format(remote_path, folder_name))
        run("sudo rm {}".format(remote_path))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(folder_name, folder_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(folder_name))
        return True
    except Exception as e:
        return False

