from base import Task
from common import phases
from common.tasks import apt


class DefaultPackages(Task):
	description = 'Adding image packages required for Azure'
	phase = phases.preparation
	predecessors = [apt.AddDefaultSources]

	@classmethod
	def run(cls, info):
		kernels = {'amd64': 'linux-image-amd64',
		           'i386':  'linux-image-686', }
		info.packages.add(kernels.get(info.manifest.system['architecture']))
        info.packages.add('openssl')
        info.packages.add('python-ssl')
		info.packages.add('openssh-server')
        info.packages.add('python-pyasn1')
        info.packages.add('waagent')
