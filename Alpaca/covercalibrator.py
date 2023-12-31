
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# covercalibrator.py - Alpaca API responders for Covercalibrator
#
# Author:   Austin M. Lankford austin@austinlankford.com (aml)
#
# -----------------------------------------------------------------------------
# Edit History:
#   Generated by Python Interface Generator for AlpycaDevice
#
# 12-14-2023   aml Initial edit

from falcon import Request, Response, HTTPBadRequest, before
from logging import Logger
from shr import PropertyResponse, MethodResponse, PreProcessRequest, \
                get_request_field, to_bool
from exceptions import *        # Nothing but exception classes
from calibratordevice import CoverCalibratorDevice

logger: Logger = None

calibrator_device = CoverCalibratorDevice()

# ----------------------
# MULTI-INSTANCE SUPPORT
# ----------------------
# If this is > 0 then it means that multiple devices of this type are supported.
# Each responder on_get() and on_put() is called with a devnum parameter to indicate
# which instance of the device (0-based) is being called by the client. Leave this
# set to 0 for the simple case of controlling only one instance of this device type.
#
maxdev = 0                      # Single instance

# -----------
# DEVICE INFO
# -----------
# Static metadata not subject to configuration changes

class CovercalibratorMetadata:
    """ Metadata describing the Covercalibrator Device."""
    Name = 'Flats panel'
    Version = '1.0.0'
    Description = 'DIY Flat Panel Calibrator'
    DeviceType = 'Covercalibrator'
    DeviceID = 'fd75206a-ccf2-4bfa-86af-637881fc6b5f'
    Info = 'Alpaca Flats Panel\nImplements ICovercalibrator\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = 1

# --------------------
# RESOURCE CONTROLLERS
# --------------------

@before(PreProcessRequest(maxdev))
class action:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandblind:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandbool:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class commandstring:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class Connected:
    def on_get(self, req: Request, resp: Response, devnum: int):
        is_conn = calibrator_device.connected
        resp.text = PropertyResponse(is_conn, req).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        conn_str = get_request_field('Connected', req)
        conn = to_bool(conn_str)  # Raises 400 Bad Request if str to bool fails
        try:
            if conn:
                calibrator_device.connect()
            else:
                calibrator_device.disconnect()
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Covercalibrator.Connected failed', ex)).json


@before(PreProcessRequest(maxdev))
class description:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(CovercalibratorMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class driverinfo:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(CovercalibratorMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class interfaceversion:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(CovercalibratorMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class driverversion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(CovercalibratorMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(CovercalibratorMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class supportedactions:
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class Brightness:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.calibrator_state == 0:
            resp.text = PropertyResponse(None, req, PropertyNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            val = calibrator_device.brightness
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req, DriverException(0x500, 'Covercalibrator.Brightness failed', ex)).json


@before(PreProcessRequest(maxdev))
class CalibratorState:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            val = calibrator_device.calibrator_state
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req, DriverException(0x500, 'Covercalibrator.Calibratorstate failed', ex)).json


@before(PreProcessRequest(maxdev))
class CoverState:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            val = calibrator_device.cover_state
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req, DriverException(0x500, 'Covercalibrator.Coverstate failed', ex)).json


@before(PreProcessRequest(maxdev))
class MaxBrightness:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.calibrator_state == 0:
            resp.text = PropertyResponse(None, req, PropertyNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            val = calibrator_device.max_brightness
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req, DriverException(0x500, 'Covercalibrator.Maxbrightness failed', ex)).json


@before(PreProcessRequest(maxdev))
class CalibratorOff:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.calibrator_state == 0:
            resp.text = MethodResponse(req, MethodNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            calibrator_device.turn_off()
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Covercalibrator.Calibratoroff failed', ex)).json


@before(PreProcessRequest(maxdev))
class calibratoron:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        brightnessstr = get_request_field('Brightness', req)      # Raises 400 bad request if missing
        try:
            brightness = int(brightnessstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Brightness " + brightnessstr + " not a valid number.')).json
            return
        if brightness < 0 or brightness > 100:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Brightness {brightness} out of range.')).json
            return
        try:
            calibrator_device.turn_on(brightness)
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Covercalibrator.Calibratoron failed', ex)).json


@before(PreProcessRequest(maxdev))
class CloseCover:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.cover_state == 0:
            resp.text = MethodResponse(req, MethodNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            calibrator_device.close_cover()
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Covercalibrator.Closecover failed', ex)).json


@before(PreProcessRequest(maxdev))
class OpenCover:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.cover_state == 0:
            resp.text = MethodResponse(req, MethodNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            calibrator_device.open_cover()
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Covercalibrator.Opencover failed', ex)).json


@before(PreProcessRequest(maxdev))
class HaltCover:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if calibrator_device.cover_state == 0:
            resp.text = MethodResponse(req, MethodNotImplementedException()).json
            return
        if not calibrator_device.connected:
            resp.text = PropertyResponse(None, req, NotConnectedException()).json
            return
        try:
            calibrator_device.halt_cover()
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req, DriverException(0x500, 'Covercalibrator.Haltcover failed', ex)).json
