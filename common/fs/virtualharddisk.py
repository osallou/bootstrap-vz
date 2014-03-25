from common.fs.qemuvolume import QEMUVolume


class VirtualHardDisk(QEMUVolume):

	extension = 'vdh'
	qemu_format = 'vpc'
	ovf_uri = None

	def get_uuid(self):
		import uuid
		with open(self.image_path) as image:
			image.seek(392)
			return uuid.UUID(bytes_le=image.read(16))
