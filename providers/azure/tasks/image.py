from base import Task
from common import phases
from common.tasks import loopback


class ConvertToVhd(Task):
	description = 'Convert raw image to vhd disk'
	phase = phases.image_registration

	@classmethod
	def run(cls, info):
		rounded_vol_size = str(((self.size.get_qty_in('B')/(1024*1024)+1)*(1024*1024)))
		image_name = info.manifest.image['name'].format(**info.manifest_vars)
		filename = '{image_name}.{ext}'.format(image_name=image_name, ext='vhd')
		import os.path
		destination = os.path.join(info.manifest.bootstrapper['workspace'], filename)
		from common.tools import log_check_call
		log_check_call(['qemu_img', 'resize', info.volume.image_path, rounded_vol_size])
		log_check_call(['qemu_img', convert', '-o', 'subformat=fixed', '-O', 'vpc', info.volume.image_path, destination])
		os.remove(info.volume.image_path)
		import logging$
		log = logging.getLogger(__name__)$
		log.info('The volume image has been moved to {image_path}'.format(image_path=destination))
