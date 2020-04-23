################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import requests
import logging

logger = logging.getLogger('dms_client')
logging.basicConfig(level=logging.INFO)

def _uri_(path):
    return f'http://127.0.0.1:8080/{path}'

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

##
## dms_version_get
##
def dms_version_get():
    try:
        response = requests.get(_uri_('version'))
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_csi_new
##
def dms_source_csi_new(name, width, height, fps_n, fps_d):
    try:
        response = requests.post(_uri_('source/csi/new'), 
            json={'name': name, 'width': width, 'height': height, 'fps_n': fps_n, 'fps_d': fps_d})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_usb_new
##
def dms_source_usb_new(name, width, height, fps_n, fps_d):
    try:
        response = requests.post(_uri_('source/usb/new'), 
            json={'name': name, 'width': width, 'height': height, 'fps_n': fps_n, 'fps_d': fps_d})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_source_uri_new
##
def dms_source_uri_new(name, uri, is_live, cudadec_mem_type, intra_decode, drop_frame_interval):
    try:
        response = requests.post(_uri_('source/uri/new'), 
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
def dms_source_rtsp_new(name, uri, protocol, cudadec_mem_type, intra_decode, drop_frame_interval):
    try:
        response = requests.post(_uri_('source/rtsp/new'), 
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
def dms_source_dimensions_get(name):
    try:
        response = requests.post(_uri_('source/dimensions/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['width'], data['height']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_source_frame_rate_get
##
def dms_source_frame_rate_get(name):
    try:
        response = requests.post(_uri_('source/frame_rate/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['fps_n'], data['fps_d']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0, 0

##
## dms_source_decode_uri_get
##
def dms_source_decode_uri_get(name):
    try:
        response = requests.post(_uri_('source/decode/uri/get'), json={'name': name})
        logger.info(response.text)
        data = response.json()
        return data['result'], data['uri']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0], 0

##
## dms_source_decode_uri_set
##
def dms_source_decode_uri_set(name, uri):
    try:
        response = requests.post(_uri_('source/decode/uri/set'), 
            json={'name': name, 'uri': uri})
        logger.info(response.text)
        data = response.json()
        return data['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_primary_new
##
def dms_gie_primary_new(name, infer_config_file, model_engine_file, interval):
    try:
        response = requests.post(_uri_('gie/primary/new'), 
            json={'name': name, 'infer_config_file': infer_config_file, 'model_engine_file': model_engine_file, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_gie_secondary_new
##
def dms_gie_secondary_new(name, infer_config_file, model_engine_file, infer_on_gie_name, interval):
    try:
        response = requests.post(_uri_('gie/secondary/new'), 
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
def dms_gie_infer_config_file_get(name):
    try:
        response = requests.post(_uri_('gie/infer_config_file/get'), 
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
def dms_gie_infer_config_file_set(name, file):
    try:
        response = requests.post(_uri_('gie/infer_config_file/set'), 
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
def dms_gie_infer_config_file_upload(file):
    try:
        response = requests.post(_uri_('gie/infer_config_file/upload'), 
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
def dms_gie_model_engine_file_get(name):
    try:
        response = requests.post(_uri_('gie/model_engine_file/get'), 
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
def dms_gie_model_engine_file_set(name, file):
    try:
        response = requests.post(_uri_('gie/model_engine_file/set'), 
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
def dms_gie_model_engine_file_upload(file):
    try:
        response = requests.post(_uri_('gie/model_engine_file/upload'), 
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
def dms_tracker_ktl_new(name, max_width, max_height):
    try:
        response = requests.post(_uri_('tracker/ktl/new'), 
            json={'name': name, 'max_width': max_width, 'max_height': max_height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tracker_iou_new
##
def dms_tracker_iou_new(name, config_file, max_width, max_height):
    try:
        response = requests.post(_uri_('tracker/iou/new'), 
            json={'name': name, 'config_file': config_file, 'max_width': max_width, 'max_height': max_height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tracker_max_dimensions_get
##
def dms_tracker_max_dimensions_get(name):
    try:
        response = requests.post(_uri_('tracker/max_dimensions/get'), 
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
def dms_tracker_max_dimensions_set(name, max_width, max_height):
    try:
        response = requests.post(_uri_('tracker/max_dimensions/set'), 
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
def dms_tiler_new(name, width, height):
    try:
        response = requests.post(_uri_('tiler/new'), 
            json={'name': name, 'width': width, 'height': height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tee_demuxer_new
##
def dms_tee_demuxer_new(name):
    try:
        response = requests.post(_uri_('tee/demuxer/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_tee_splitter_new
##
def dms_tee_splitter_new(name):
    try:
        response = requests.post(_uri_('tee/splitter/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_new
##
def dms_osd_new(name, is_clock_enabled):
    try:
        response = requests.post(_uri_('osd/new'), 
            json={'name': name, 'is_clock_enabled': is_clock_enabled})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_osd_redaction_enabled_get
##
def dms_osd_redaction_enabled_get(name):
    try:
        response = requests.post(_uri_('osd/redaction/enabled/get'), 
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
def dms_osd_redaction_enabled_set(name, enabled):
    try:
        response = requests.post(_uri_('osd/redaction/enabled/set'),
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
def dms_osd_redaction_class_add(name, class_id, red, green, blue, alpha):
    try:
        response = requests.post(_uri_('osd/redaction/classid/add'), 
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
def dms_osd_redaction_class_remove(name, class_id):
    try:
        response = requests.post(_uri_('osd/redaction/classid/remove'),
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
def dms_sink_fake_new(name):
    try:
        response = requests.post(_uri_('sink/fake/new'), 
            json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_overlay_new
##
def dms_sink_overlay_new(name, overlay_id, display_id, depth, offsetX, offsetY, width, height):
    try:
        response = requests.post(_uri_('sink/overlay/new'), 
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
def dms_sink_window_new(name, offsetX, offsetY, width, height):
    try:
        response = requests.post(_uri_('sink/window/new'), 
            json={'name': name, 'offsetX': offsetX, 'offsetY': offsetY, 'width': width, 'height': height})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_sink_file_new
##
def dms_sink_file_new(name, filepath, codec, container, bitrate, interval):
    try:
        response = requests.post(_uri_('sink/file/new'), 
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
def dms_sink_image_new(name, outdir):
    try:
        response = requests.post(_uri_('sink/image/new'), 
            json={'name': name, 'outdir': outdir})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dsm_sink_image_frame_capture_enabled_get
##
def dms_sink_image_frame_capture_enabled_get(name):
    try:
        response = requests.post(_uri_('sink/image/frame_capture/enabled/get'), 
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
def dms_sink_image_frame_capture_enabled_set(name, enabled):
    try:
        response = requests.post(_uri_('sink/image/frame_capture/enabled/set'),
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
def dms_sink_image_frame_capture_interval_get(name):
    try:
        response = requests.post(_uri_('sink/image/frame_capture/interval/get'), 
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
def dms_sink_image_frame_capture_interval_set(name, interval):
    try:
        response = requests.post(_uri_('sink/image/frame_capture/interval/set'),
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
def dms_sink_image_object_capture_enabled_get(name):
    try:
        response = requests.post(_uri_('sink/image/object_capture/enabled/get'), 
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
def dms_sink_image_object_capture_enabled_set(name, enabled):
    try:
        response = requests.post(_uri_('sink/image/object_capture/enabled/set'),
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
def dms_sink_image_object_capture_class_add(name, class_id, full_frame, capture_limit):
    try:
        response = requests.post(_uri_('sink/image/object_capture/classid/add'), 
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
def dms_sink_image_object_capture_class_remove(name, class_id):
    try:
        response = requests.post(_uri_('sink/image/object_capture/classid/remove'),
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
def dms_sink_rtsp_new(name, host, udp_port, rtmp_port, codec, bitrate, interval):
    try:
        response = requests.post(_uri_('sink/rtsp/new'), 
            json={'name': name, 'host': host, 'udp_port': udp_port,
            'rtmp_port': rtmp_port, 'codec': codec, 'bitrate': bitrate, 'interval': interval})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_new
##
def dms_branch_new(name):
    try:
        response = requests.post(_uri_('branch/new'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_component_add
##
def dms_branch_component_add(branch, component):
    try:
        response = requests.post(_uri_('branch/component/add'), json={'branch': branch, 'component': component})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_branch_component_add_many
##
def dms_branch_component_add_many(branch, components):
    try:
        response = requests.post(_uri_('branch/component/add/many'), json={'branch': branch, 'components': components})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_new
##
def dms_pipeline_new(name):
    try:
        response = requests.post(_uri_('pipeline/new'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_delete
##
def dms_pipeline_delete(name):
    try:
        response = requests.post(_uri_('pipeline/delete'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_delete_all
##
def dms_pipeline_delete_all():
    try:
        response = requests.post(_uri_('pipeline/delete/all'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_component_add
##
def dms_pipeline_component_add(pipeline, component):
    try:
        response = requests.post(_uri_('pipeline/component/add'), json={'pipeline': pipeline, 'component': component})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_component_add_many
##
def dms_pipeline_component_add_many(pipeline, components):
    try:
        response = requests.post(_uri_('pipeline/component/add/many'), json={'pipeline': pipeline, 'components': components})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_pipeline_play
##
def dms_pipeline_play(name):
    try:
        response = requests.post(_uri_('pipeline/play'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_component_delete
##
def dms_component_delete(name):
    try:
        response = requests.post(_uri_('component/delete'), json={'name': name})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_component_delete_all
##
def dms_component_delete_all():
    try:
        response = requests.post(_uri_('component/delete/all'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_main_loop_run
##
def dms_main_loop_run():
    try:
        response = requests.post(_uri_('main_loop/run'), json={})
        logger.info(response.text)
        return response.json()['result']
    except:
        logger.error(sys.exc_info()[0])
        return sys.exc_info()[0]

##
## dms_main_loop_quit
##
def dms_main_loop_quit():
    try:
        requests.post(_uri_('main_loop/quit'), json={})
    except:
        logger.error(sys.exc_info()[0])
