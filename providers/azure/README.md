KVM provider
===========

This provider generates raw images for KVM.
It also supports an optional virtio integration.

Setup
=====

Needs nbd module loaded:

    modprobe nbd max_part=3

qemu-img >= 1.7.0 required to convert raw image to vhd fixed size disk.
This release is available in wheezy-backports.


Virtio
======

Add to bootstrapper the list of virtio modules to load, example:

    "virtio" : [ "virtio_pci", "virtio_blk" ]

