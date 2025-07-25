# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T11:19:22+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, HTTPBasic
from fastapi import Path, Query
from pydantic import conint, constr
from starlette.requests import Request

from models import (
    CompositionEnumStatus,
    GroupingSid,
    RecordingEnumStatus,
    RecordingEnumType,
    RoomEnumRoomStatus,
    RoomParticipantEnumStatus,
    RoomRecordingEnumStatus,
    V1CompositionHooksGetResponse,
    V1CompositionsGetResponse,
    V1RecordingsGetResponse,
    V1RoomsGetResponse,
    V1RoomsRoomSidParticipantsGetResponse,
    V1RoomsRoomSidParticipantsParticipantSidPublishedTracksGetResponse,
    V1RoomsRoomSidParticipantsParticipantSidSubscribedTracksGetResponse,
    V1RoomsRoomSidRecordingsGetResponse,
    VideoV1Composition,
    VideoV1CompositionHook,
    VideoV1CompositionSettings,
    VideoV1Recording,
    VideoV1RecordingSettings,
    VideoV1Room,
    VideoV1RoomRoomParticipant,
    VideoV1RoomRoomParticipantRoomParticipantAnonymize,
    VideoV1RoomRoomParticipantRoomParticipantPublishedTrack,
    VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack,
    VideoV1RoomRoomParticipantRoomParticipantSubscribeRule,
    VideoV1RoomRoomRecording,
    VideoV1RoomRoomRecordingRule,
)

app = MCPProxy(
    contact={
        'email': 'support@twilio.com',
        'name': 'Twilio Support',
        'url': 'https://support.twilio.com',
    },
    description='This is the public Twilio REST API.',
    license={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    termsOfService='https://www.twilio.com/legal/tos',
    title='Twilio - Video',
    version='1.42.0',
    servers=[{'url': 'https://video.twilio.com'}],
)


@app.get(
    '/v1/CompositionHooks',
    description=""" List of all Recording CompositionHook resources. """,
    tags=[
        'composition_management',
        'recording_management',
        'room_management',
        'room_participant_management',
        'room_specific_recording_rule_management',
        'room_recording_management',
    ],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_composition_hook(
    enabled: Optional[bool] = Query(None, alias='Enabled'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    friendly_name: Optional[str] = Query(None, alias='FriendlyName'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/CompositionHooks',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def create_composition_hook(request: Request):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/CompositionHooks/{Sid}',
    description=""" Delete a Recording CompositionHook resource identified by a `CompositionHook SID`. """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def delete_composition_hook(
    sid: constr(pattern=r'^HK[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/CompositionHooks/{Sid}',
    description=""" Returns a single CompositionHook resource identified by a CompositionHook SID. """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_composition_hook(
    sid: constr(pattern=r'^HK[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/CompositionHooks/{Sid}',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_composition_hook(
    sid: constr(pattern=r'^HK[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    ),
    request: Request = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/CompositionSettings/Default',
    tags=['room_management', 'room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_composition_settings():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/CompositionSettings/Default',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def create_composition_settings(request: Request):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Compositions',
    description=""" List of all Recording compositions. """,
    tags=['room_management', 'room_specific_recording_rule_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_composition(
    status: Optional[CompositionEnumStatus] = Query(None, alias='Status'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    room_sid: Optional[
        constr(pattern=r'^RM[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Query(None, alias='RoomSid'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Compositions',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def create_composition(request: Request):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/Compositions/{Sid}',
    description=""" Delete a Recording Composition resource identified by a Composition SID. """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def delete_composition(
    sid: constr(pattern=r'^CJ[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Compositions/{Sid}',
    description=""" Returns a single Composition resource identified by a Composition SID. """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_composition(
    sid: constr(pattern=r'^CJ[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/RecordingSettings/Default',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_recording_settings():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/RecordingSettings/Default',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def create_recording_settings(request: Request):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Recordings',
    description=""" List of all Track recordings. """,
    tags=['recording_management', 'room_recording_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_recording(
    status: Optional[RecordingEnumStatus] = Query(None, alias='Status'),
    source_sid: Optional[
        constr(pattern=r'^[a-zA-Z]{2}[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Query(None, alias='SourceSid'),
    grouping_sid: Optional[GroupingSid] = Query(None, alias='GroupingSid'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    media_type: Optional[RecordingEnumType] = Query(None, alias='MediaType'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/Recordings/{Sid}',
    description=""" Delete a Recording resource identified by a Recording SID. """,
    tags=['room_management', 'room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def delete_recording(
    sid: constr(pattern=r'^RT[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Recordings/{Sid}',
    description=""" Returns a single Recording resource identified by a Recording SID. """,
    tags=['room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_recording(
    sid: constr(pattern=r'^RT[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    )
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_room(
    status: Optional[RoomEnumRoomStatus] = Query(None, alias='Status'),
    unique_name: Optional[str] = Query(None, alias='UniqueName'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def create_room(request: Request):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants',
    tags=['room_management', 'room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_room_participant(
    room_sid: str = Path(..., alias='RoomSid'),
    status: Optional[RoomParticipantEnumStatus] = Query(None, alias='Status'),
    identity: Optional[str] = Query(None, alias='Identity'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks',
    description=""" Returns a list of tracks associated with a given Participant. Only `currently` Published Tracks are in the list resource. """,
    tags=['room_participant_management', 'room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_room_participant_published_track(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid}',
    description=""" Returns a single Track resource represented by TrackName or SID. """,
    tags=['room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_participant_published_track(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
    sid: str = Path(..., alias='Sid'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules',
    description=""" Returns a list of Subscribe Rules for the Participant. """,
    tags=['room_management', 'room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_participant_subscribe_rule(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules',
    description=""" Update the Subscribe Rules for the Participant """,
    tags=['room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_room_participant_subscribe_rule(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
    request: Request = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks',
    description=""" Returns a list of tracks that are subscribed for the participant. """,
    tags=['room_participant_management', 'room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_room_participant_subscribed_track(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks/{Sid}',
    description=""" Returns a single Track resource represented by `track_sid`.  Note: This is one resource with the Video API that requires a SID, be Track Name on the subscriber side is not guaranteed to be unique. """,
    tags=['room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_participant_subscribed_track(
    room_sid: str = Path(..., alias='RoomSid'),
    participant_sid: str = Path(..., alias='ParticipantSid'),
    sid: constr(pattern=r'^MT[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    ),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Participants/{Sid}',
    tags=['room_management', 'room_recording_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_participant(
    room_sid: str = Path(..., alias='RoomSid'), sid: str = Path(..., alias='Sid')
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms/{RoomSid}/Participants/{Sid}',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_room_participant(
    room_sid: str = Path(..., alias='RoomSid'),
    sid: str = Path(..., alias='Sid'),
    request: Request = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_room_participant_anonymize(
    room_sid: str = Path(..., alias='RoomSid'), sid: str = Path(..., alias='Sid')
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/RecordingRules',
    description=""" Returns a list of Recording Rules for the Room. """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_recording_rule(room_sid: str = Path(..., alias='RoomSid')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms/{RoomSid}/RecordingRules',
    description=""" Update the Recording Rules for the Room """,
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_room_recording_rule(
    room_sid: str = Path(..., alias='RoomSid'), request: Request = ...
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Recordings',
    tags=['room_recording_management', 'room_management', 'recording_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_room_recording(
    room_sid: constr(
        pattern=r'^RM[0-9a-fA-F]{32}$', min_length=34, max_length=34
    ) = Path(..., alias='RoomSid'),
    status: Optional[RoomRecordingEnumStatus] = Query(None, alias='Status'),
    source_sid: Optional[
        constr(pattern=r'^[a-zA-Z]{2}[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Query(None, alias='SourceSid'),
    date_created_after: Optional[datetime] = Query(None, alias='DateCreatedAfter'),
    date_created_before: Optional[datetime] = Query(None, alias='DateCreatedBefore'),
    page_size: Optional[conint(ge=1, le=1000)] = Query(None, alias='PageSize'),
    page: Optional[conint(ge=0)] = Query(None, alias='Page'),
    page_token: Optional[str] = Query(None, alias='PageToken'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/Rooms/{RoomSid}/Recordings/{Sid}',
    tags=[
        'room_management',
        'room_participant_management',
        'room_recording_management',
    ],
    security=[
        HTTPBasic(name="None"),
    ],
)
def delete_room_recording(
    room_sid: constr(
        pattern=r'^RM[0-9a-fA-F]{32}$', min_length=34, max_length=34
    ) = Path(..., alias='RoomSid'),
    sid: constr(pattern=r'^RT[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    ),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{RoomSid}/Recordings/{Sid}',
    tags=['room_management', 'room_recording_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room_recording(
    room_sid: constr(
        pattern=r'^RM[0-9a-fA-F]{32}$', min_length=34, max_length=34
    ) = Path(..., alias='RoomSid'),
    sid: constr(pattern=r'^RT[0-9a-fA-F]{32}$', min_length=34, max_length=34) = Path(
        ..., alias='Sid'
    ),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/Rooms/{Sid}',
    tags=['room_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def fetch_room(sid: str = Path(..., alias='Sid')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/Rooms/{Sid}',
    tags=['room_participant_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_room(sid: str = Path(..., alias='Sid'), request: Request = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
