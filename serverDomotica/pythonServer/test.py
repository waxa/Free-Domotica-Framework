#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GCMPush import GCMPush

idTest = "APA91bElBpkPMFmBX6kaifE_oPcMCXJu1lyTaW-zQKlHtDJM6PB-LzeAXFojMyYVPJ0g8E5_TmSBwku0W_8i1iKCgGMEMJrQleJtClriWS_O3EQeyQQRVjt5pt68QNNX-3YGgxKU-uBlRUClKci8pr9AQxO1u2ihGA"
servKey = "AIzaSyCw_KuynDE61IJpeRYgssTHjZFWxo14RAg"

GCMPushService = GCMPush(servKey, True)

GCMPushService.push([idTest], "test title", "test message")