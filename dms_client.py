################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import requests
import logging

logger = logging.getLogger('dms_client')
logging.basicConfig(level=logging.INFO)

DMS_RTP_TCP = 4
DMS_RTP_ALL = 7

DMS_CUDADEC_MEMTYPE_DEVICE = 0
DMS_CUDADEC_MEMTYPE_PINNED = 1
DMS_CUDADEC_MEMTYPE_UNIFIED = 2

DMS_SOURCE_CODEC_PARSER_H264 = 0
DMS_SOURCE_CODEC_PARSER_H265 = 1

DMS_CODEC_H264 = 0
DMS_CODEC_H265 = 1
DMS_CODEC_MPEG4 = 2

DMS_CONTAINER_MP4 = 0
DMS_CONTAINER_MKV = 1

# Active targets - [name: url] pairs
targets = {}

##
## _url_ assembles a service request path from 
##  a target's base URL and path to service API
##
def _url_(target, path):

    # ensure target existance
    if target not in targets:
        raise ValueError
        
    url = os.path.join(targets[target], path)
    logger.info('Target = {t}, API = {a}'.format(t=target,a=url))
    return url


##
## dms_target_net
##
def dms_target_new(name, url):
    try:
        targets[name]=url
        return 'DSL_RESULT_SUCCESS'
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_target_version_get
##
def dms_target_version_get(target):
    try:
        response = requests.get(_url_(target, 'version'))
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_csi_new
##
def dms_source_csi_new(target, name, width, height, fps_n, fps_d):
    try:
        response = requests.post(_url_(target, 'source/csi/new'), 
            json={'name': name, 'width': width, 'height': height, 'fps_n': fps_n, 'fps_d': fps_d})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_usb_new
##
def dms_source_usb_new(target, name, width, height, fps_n, fps_d):
    try:
        response = requests.post(_url_(target, 'source/usb/new'), 
            json={'name': name, 'width': width, 'height': height, 'fps_n': fps_n, 'fps_d': fps_d})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_uri_new
##
def dms_source_uri_new(target, name, uri, is_live, cudadec_mem_type, intra_decode, drop_frame_interval):
    try:
        response = requests.post(_url_(target, 'source/uri/new'), 
            json={'name': name, 'uri': uri, 'is_live': is_live, 'cudadec_mem_type': cudadec_mem_type,
                'intra_decode': intra_decode, 'drop_frame_interval': drop_frame_interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_rtsp_new
##
def dms_source_rtsp_new(target, name, uri, protocol, cudadec_mem_type, intra_decode, drop_frame_interval):
    try:
        response = requests.post(_url_(target, 'source/rtsp/new'), 
            json={'name': name, 'uri': uri, 'protocol': protocol, 'cudadec_mem_type': cudadec_mem_type,
                'intra_decode': intra_decode, 'drop_frame_interval': drop_frame_interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_dimensions_get
##
def dms_source_dimensions_get(target, name):
    try:
        response = requests.post(_url_(target, 'source/dimensions/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['width'], data['height']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_source_frame_rate_get
##
def dms_source_frame_rate_get(target, name):
    try:
        response = requests.post(_url_(target, 'source/frame_rate/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['fps_n'], data['fps_d']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_source_decode_uri_get
##
def dms_source_decode_uri_get(target, name):
    try:
        response = requests.post(_url_(target, 'source/decode/uri/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['uri']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_source_decode_uri_set
##
def dms_source_decode_uri_set(target, name, uri):
    try:
        response = requests.post(_url_(target, 'source/decode/uri/set'), 
            json={'name': name, 'uri': uri})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_num_in_use_get
##
def dms_source_num_in_use_get(target):
    try:
        response = requests.get(_url_(target, 'source/num_in_use/get'))
        logger.info(response.text)
        data = response.json()
        return data['num']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_num_in_use_max_get
##
def dms_source_num_in_use_max_get(target):
    try:
        response = requests.get(_url_(target, 'source/num_in_use/max/get'))
        logger.info(response.text)
        data = response.json()
        return data['num']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_num_in_use_max_set
##
def dms_source_num_in_use_max_set(target, num):
    try:
        response = requests.post(_url_(target, 'source/num_in_use/max/set'), 
            json={'num': num})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_primary_new
##
def dms_gie_primary_new(target, name, infer_config_file, model_engine_file, interval):
    try:
        response = requests.post(_url_(target, 'gie/primary/new'), 
            json={'name': name, 'infer_config_file': infer_config_file, 'model_engine_file': model_engine_file, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_secondary_new
##
def dms_gie_secondary_new(target, name, infer_config_file, model_engine_file, infer_on_gie_name, interval):
    try:
        response = requests.post(_url_(target, 'gie/secondary/new'), 
            json={'name': name, 'infer_config_file': infer_config_file, 'model_engine_file': model_engine_file,
            'infer_on_gie_name': infer_on_gie_name, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_infer_config_file_get
##
def dms_gie_infer_config_file_get(target, name):
    try:
        response = requests.post(_url_(target, 'gie/infer_config_file/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['file']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_infer_config_file_set
##
def dms_gie_infer_config_file_set(target, name, file):
    try:
        response = requests.post(_url_(target, 'gie/infer_config_file/set'), 
            json={'name': name, 'file': file})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_infer_config_file_upload
##
def dms_gie_infer_config_file_upload(target, file):
    try:
        response = requests.post(_url_(target, 'gie/infer_config_file/upload'), 
            files={'ufile': open(file, 'rb')})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_model_engine_file_get
##
def dms_gie_model_engine_file_get(target, name):
    try:
        response = requests.post(_url_(target, 'gie/model_engine_file/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['file']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_model_engine_file_set
##
def dms_gie_model_engine_file_set(target, name, file):
    try:
        response = requests.post(_url_(target, 'gie/model_engine_file/set'), 
            json={'name': name, 'file': file})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_model_engine_file_upload
##
def dms_gie_model_engine_file_upload(target, file):
    try:
        response = requests.post(_url_(target, 'gie/model_engine_file/upload'), 
            files={'ufile': open(file, 'rb')})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tracker_ktl_new
##
def dms_tracker_ktl_new(target, name, max_width, max_height):
    try:
        response = requests.post(_url_(target, 'tracker/ktl/new'), 
            json={'name': name, 'max_width': max_width, 'max_height': max_height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tracker_iou_new
##
def dms_tracker_iou_new(target, name, config_file, max_width, max_height):
    try:
        response = requests.post(_url_(target, 'tracker/iou/new'), 
            json={'name': name, 'config_file': config_file, 'max_width': max_width, 'max_height': max_height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tracker_max_dimensions_get
##
def dms_tracker_max_dimensions_get(target, name):
    try:
        response = requests.post(_url_(target, 'tracker/max_dimensions/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['max_width'], data['max_height']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_tracker_max_dimensions_set
##
def dms_tracker_max_dimensions_set(target, name, max_width, max_height):
    try:
        response = requests.post(_url_(target, 'tracker/max_dimensions/set'), 
            json={'name': name, 'max_width': max_width, 'max_height': max_height})
        print(response.text)
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tiler_new
##
def dms_tiler_new(target, name, width, height):
    try:
        response = requests.post(_url_(target, 'tiler/new'), 
            json={'name': name, 'width': width, 'height': height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tee_demuxer_new
##
def dms_tee_demuxer_new(target, name):
    try:
        response = requests.post(_url_(target, 'tee/demuxer/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tee_splitter_new
##
def dms_tee_splitter_new(target, name):
    try:
        response = requests.post(_url_(target, 'tee/splitter/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_new
##
def dms_osd_new(target, name, is_clock_enabled):
    try:
        response = requests.post(_url_(target, 'osd/new'), 
            json={'name': name, 'is_clock_enabled': is_clock_enabled})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_redaction_enabled_get
##
def dms_osd_redaction_enabled_get(target, name):
    try:
        response = requests.post(_url_(target, 'osd/redaction/enabled/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['enabled']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_osd_redaction_enabled_set
##
def dms_osd_redaction_enabled_set(target, name, enabled):
    try:
        response = requests.post(_url_(target, 'osd/redaction/enabled/set'),
            json={'name': name, 'enabled': enabled})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_clock_enabled_get
##
def dms_osd_clock_enabled_get(target, name):
    try:
        response = requests.post(_url_(target, 'osd/clock/enabled/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['enabled']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_osd_clock_enabled_set
##
def dms_osd_clock_enabled_set(target, name, enabled):
    try:
        response = requests.post(_url_(target, 'osd/clock/enabled/set'),
            json={'name': name, 'enabled': enabled})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_redaction_class_add
##
def dms_osd_redaction_class_add(target, name, class_id, red, green, blue, alpha):
    try:
        response = requests.post(_url_(target, 'osd/redaction/classid/add'), 
            json={'name': name, 'class_id': class_id, 
            'red': red, 'green': green, 'blue': blue, 'alpha': alpha})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_redaction_class_remove
##
def dms_osd_redaction_class_remove(target, name, class_id):
    try:
        response = requests.post(_url_(target, 'osd/redaction/classid/remove'),
            json={'name': name, 'class_id': class_id})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_fake_new
##
def dms_sink_fake_new(target, name):
    try:
        response = requests.post(_url_(target, 'sink/fake/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_overlay_new
##
def dms_sink_overlay_new(target, name, overlay_id, display_id, depth, offsetX, offsetY, width, height):
    try:
        response = requests.post(_url_(target, 'sink/overlay/new'), 
            json={'name': name, 'overlay_id': overlay_id, 'display_id': display_id, 
            'depth': depth, 'offsetX': offsetX, 'offsetY': offsetY, 'width': width, 'height': height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_window_new
##
def dms_sink_window_new(target, name, offsetX, offsetY, width, height):
    try:
        response = requests.post(_url_(target, 'sink/window/new'), 
            json={'name': name, 'offsetX': offsetX, 'offsetY': offsetY, 'width': width, 'height': height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_file_new
##
def dms_sink_file_new(target, name, filepath, codec, container, bitrate, interval):
    try:
        response = requests.post(_url_(target, 'sink/file/new'), 
            json={'name': name, 'filepath': filepath, 'codec': codec,
            'container': container, 'bitrate': bitrate, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_image_new
##
def dms_sink_image_new(target, name, outdir):
    try:
        response = requests.post(_url_(target, 'sink/image/new'), 
            json={'name': name, 'outdir': outdir})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dsm_sink_image_frame_capture_enabled_get
##
def dms_sink_image_frame_capture_enabled_get(target, name):
    try:
        response = requests.post(_url_(target, 'sink/image/frame_capture/enabled/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['enabled']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dsm_sink_image_frame_capture_enabled_set
##
def dms_sink_image_frame_capture_enabled_set(target, name, enabled):
    try:
        response = requests.post(_url_(target, 'sink/image/frame_capture/enabled/set'),
            json={'name': name, 'enabled': enabled})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dsm_sink_image_frame_capture_interval_get
##
def dms_sink_image_frame_capture_interval_get(target, name):
    try:
        response = requests.post(_url_(target, 'sink/image/frame_capture/interval/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['interval']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dsm_sink_image_frame_capture_interval_set
##
def dms_sink_image_frame_capture_interval_set(target, name, interval):
    try:
        response = requests.post(_url_(target, 'sink/image/frame_capture/interval/set'),
            json={'name': name, 'interval': interval})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dsm_sink_image_object_capture_enabled_get
##
def dms_sink_image_object_capture_enabled_get(target, name):
    try:
        response = requests.post(_url_(target, 'sink/image/object_capture/enabled/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['enabled']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dsm_sink_image_object_capture_enabled_set
##
def dms_sink_image_object_capture_enabled_set(target, name, enabled):
    try:
        response = requests.post(_url_(target, 'sink/image/object_capture/enabled/set'),
            json={'name': name, 'enabled': enabled})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dsm_sink_image_object_capture_class_add
##
def dms_sink_image_object_capture_class_add(target, name, class_id, full_frame, capture_limit):
    try:
        response = requests.post(_url_(target, 'sink/image/object_capture/classid/add'), 
            json={'name': name, 'class_id': class_id, 'full_frame': full_frame, 'capture_limit': capture_limit})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_image_object_capture_class_remove
##
def dms_sink_image_object_capture_class_remove(target, name, class_id):
    try:
        response = requests.post(_url_(target, 'sink/image/object_capture/classid/remove'),
            json={'name': name, 'class_id': class_id})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_rtsp_new
##
def dms_sink_rtsp_new(target, name, host, udp_port, rtmp_port, codec, bitrate, interval):
    try:
        response = requests.post(_url_(target, 'sink/rtsp/new'), 
            json={'name': name, 'host': host, 'udp_port': udp_port,
            'rtmp_port': rtmp_port, 'codec': codec, 'bitrate': bitrate, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_num_in_use_get
##
def dms_sink_num_in_use_get(target):
    try:
        response = requests.get(_url_(target, 'sink/num_in_use/get'))
        logger.info(response.text)
        data = response.json()
        return data['num']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_num_in_use_max_get
##
def dms_sink_num_in_use_max_get(target):
    try:
        response = requests.get(_url_(target, 'sink/num_in_use/max/get'))
        logger.info(response.text)
        data = response.json()
        return data['num']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_num_in_use_max_set
##
def dms_sink_num_in_use_max_set(target, num):
    try:
        response = requests.post(_url_(target, 'sink/num_in_use/max/set'), 
            json={'num': num})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_new
##
def dms_branch_new(target, name):
    try:
        response = requests.post(_url_(target, 'branch/new'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_component_add
##
def dms_branch_component_add(target, branch, component):
    try:
        response = requests.post(_url_(target, 'branch/component/add'), json={'branch': branch, 'component': component})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_component_add_many
##
def dms_branch_component_add_many(target, branch, components):
    try:
        response = requests.post(_url_(target, 'branch/component/add/many'), json={'branch': branch, 'components': components})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_new
##
def dms_pipeline_new(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/new'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_delete
##
def dms_pipeline_delete(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/delete'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_delete_all
##
def dms_pipeline_delete_all(target):
    try:
        response = requests.post(_url_(target, 'pipeline/delete/all'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_component_add
##
def dms_pipeline_component_add(target, pipeline, component):
    try:
        response = requests.post(_url_(target, 'pipeline/component/add'), 
            json={'pipeline': pipeline, 'component': component})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_component_add_many
##
def dms_pipeline_component_add_many(target, pipeline, components):
    try:
        response = requests.post(_url_(target, 'pipeline/component/add/many'), 
            json={'pipeline': pipeline, 'components': components})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_play
##
def dms_pipeline_play(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/play'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_pause
##
def dms_pipeline_pause(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/pause'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_stop
##
def dms_pipeline_stop(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/stop'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_state_get
##
def dms_pipeline_state_get(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/state_get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['state']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_pipeline_is_live
##
def dms_pipeline_is_live(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/is_live'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['is_live']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_pipeline_streammux_batch_properties_get
##
def dms_pipeline_streammux_batch_properties_get(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/batch_properties/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['batch_size'], data['batch_timeout']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_pipeline_streammux_batch_properties_set
##
def dms_pipeline_streammux_batch_properties_set(target, name, batch_size, batch_timeout):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/batch_properties/set'), 
            json={'name': name, 'batch_size': batch_size, 'batch_timeout': batch_timeout})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_streammux_dimensions_get
##
def dms_pipeline_streammux_dimensions_get(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/dimensions/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['width'], data['height']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_pipeline_streammux_dimensions_set
##
def dms_pipeline_streammux_dimensions_set(target, name, width, height):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/dimensions/set'), 
            json={'name': name, 'width': width, 'height': height})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_streammux_padding_get
##
def dms_pipeline_streammux_padding_get(target, name):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/padding/get'), 
            json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['enabled']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_pipeline_streammux_padding_set
##
def dms_pipeline_streammux_padding_set(target, name, enabled):
    try:
        response = requests.post(_url_(target, 'pipeline/streammux/padding/set'), 
            json={'name': name, 'enabled': enabled})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_component_delete
##
def dms_component_delete(target, name):
    try:
        response = requests.post(_url_(target, 'component/delete'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_component_delete_all
##
def dms_component_delete_all(target):
    try:
        response = requests.post(_url_(target, 'component/delete/all'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_main_loop_run
##
def dms_main_loop_run(target):
    try:
        response = requests.post(_url_(target, 'main_loop/run'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_main_loop_quit
##
def dms_main_loop_quit(target):
    try:
        requests.post(_url_(target, 'main_loop/quit'), json={})
    except:
        logger.error(sys.exc_info()[0])
