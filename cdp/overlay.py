# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Overlay (experimental)

from __future__ import annotations
from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from . import dom
from . import page
from . import runtime


@dataclass
class HighlightConfig:
    '''
    Configuration data for the highlighting of page elements.
    '''
    #: Whether the node info tooltip should be shown (default: false).
    show_info: typing.Optional[bool] = None

    #: Whether the node styles in the tooltip (default: false).
    show_styles: typing.Optional[bool] = None

    #: Whether the rulers should be shown (default: false).
    show_rulers: typing.Optional[bool] = None

    #: Whether the extension lines from node to the rulers should be shown (default: false).
    show_extension_lines: typing.Optional[bool] = None

    #: The content box highlight fill color (default: transparent).
    content_color: typing.Optional[dom.RGBA] = None

    #: The padding highlight fill color (default: transparent).
    padding_color: typing.Optional[dom.RGBA] = None

    #: The border highlight fill color (default: transparent).
    border_color: typing.Optional[dom.RGBA] = None

    #: The margin highlight fill color (default: transparent).
    margin_color: typing.Optional[dom.RGBA] = None

    #: The event target element highlight fill color (default: transparent).
    event_target_color: typing.Optional[dom.RGBA] = None

    #: The shape outside fill color (default: transparent).
    shape_color: typing.Optional[dom.RGBA] = None

    #: The shape margin fill color (default: transparent).
    shape_margin_color: typing.Optional[dom.RGBA] = None

    #: The grid layout color (default: transparent).
    css_grid_color: typing.Optional[dom.RGBA] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.show_info is not None:
            json['showInfo'] = self.show_info
        if self.show_styles is not None:
            json['showStyles'] = self.show_styles
        if self.show_rulers is not None:
            json['showRulers'] = self.show_rulers
        if self.show_extension_lines is not None:
            json['showExtensionLines'] = self.show_extension_lines
        if self.content_color is not None:
            json['contentColor'] = self.content_color.to_json()
        if self.padding_color is not None:
            json['paddingColor'] = self.padding_color.to_json()
        if self.border_color is not None:
            json['borderColor'] = self.border_color.to_json()
        if self.margin_color is not None:
            json['marginColor'] = self.margin_color.to_json()
        if self.event_target_color is not None:
            json['eventTargetColor'] = self.event_target_color.to_json()
        if self.shape_color is not None:
            json['shapeColor'] = self.shape_color.to_json()
        if self.shape_margin_color is not None:
            json['shapeMarginColor'] = self.shape_margin_color.to_json()
        if self.css_grid_color is not None:
            json['cssGridColor'] = self.css_grid_color.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> HighlightConfig:
        return cls(
            show_info=bool(json['showInfo']) if 'showInfo' in json else None,
            show_styles=bool(json['showStyles']) if 'showStyles' in json else None,
            show_rulers=bool(json['showRulers']) if 'showRulers' in json else None,
            show_extension_lines=bool(json['showExtensionLines']) if 'showExtensionLines' in json else None,
            content_color=dom.RGBA.from_json(json['contentColor']) if 'contentColor' in json else None,
            padding_color=dom.RGBA.from_json(json['paddingColor']) if 'paddingColor' in json else None,
            border_color=dom.RGBA.from_json(json['borderColor']) if 'borderColor' in json else None,
            margin_color=dom.RGBA.from_json(json['marginColor']) if 'marginColor' in json else None,
            event_target_color=dom.RGBA.from_json(json['eventTargetColor']) if 'eventTargetColor' in json else None,
            shape_color=dom.RGBA.from_json(json['shapeColor']) if 'shapeColor' in json else None,
            shape_margin_color=dom.RGBA.from_json(json['shapeMarginColor']) if 'shapeMarginColor' in json else None,
            css_grid_color=dom.RGBA.from_json(json['cssGridColor']) if 'cssGridColor' in json else None,
        )


class InspectMode(enum.Enum):
    SEARCH_FOR_NODE = "searchForNode"
    SEARCH_FOR_UA_SHADOW_DOM = "searchForUAShadowDOM"
    CAPTURE_AREA_SCREENSHOT = "captureAreaScreenshot"
    SHOW_DISTANCES = "showDistances"
    NONE = "none"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> InspectMode:
        return cls(json)


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disables domain notifications.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.disable',
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enables domain notifications.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.enable',
    }
    json = yield cmd_dict


def get_highlight_object_for_test(
        node_id: dom.NodeId,
        include_distance: typing.Optional[bool] = None,
        include_style: typing.Optional[bool] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,dict]:
    '''
    For testing.

    :param node_id: Id of the node to get highlight object for.
    :param include_distance: *(Optional)* Whether to include distance info.
    :param include_style: *(Optional)* Whether to include style info.
    :returns: Highlight data for the node.
    '''
    params: T_JSON_DICT = dict()
    params['nodeId'] = node_id.to_json()
    if include_distance is not None:
        params['includeDistance'] = include_distance
    if include_style is not None:
        params['includeStyle'] = include_style
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.getHighlightObjectForTest',
        'params': params,
    }
    json = yield cmd_dict
    return dict(json['highlight'])


def hide_highlight() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Hides any highlight.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.hideHighlight',
    }
    json = yield cmd_dict


def highlight_frame(
        frame_id: page.FrameId,
        content_color: typing.Optional[dom.RGBA] = None,
        content_outline_color: typing.Optional[dom.RGBA] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Highlights owner element of the frame with given id.

    :param frame_id: Identifier of the frame to highlight.
    :param content_color: *(Optional)* The content box highlight fill color (default: transparent).
    :param content_outline_color: *(Optional)* The content box highlight outline color (default: transparent).
    '''
    params: T_JSON_DICT = dict()
    params['frameId'] = frame_id.to_json()
    if content_color is not None:
        params['contentColor'] = content_color.to_json()
    if content_outline_color is not None:
        params['contentOutlineColor'] = content_outline_color.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.highlightFrame',
        'params': params,
    }
    json = yield cmd_dict


def highlight_node(
        highlight_config: HighlightConfig,
        node_id: typing.Optional[dom.NodeId] = None,
        backend_node_id: typing.Optional[dom.BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None,
        selector: typing.Optional[str] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
    objectId must be specified.

    :param highlight_config: A descriptor for the highlight appearance.
    :param node_id: *(Optional)* Identifier of the node to highlight.
    :param backend_node_id: *(Optional)* Identifier of the backend node to highlight.
    :param object_id: *(Optional)* JavaScript object id of the node to be highlighted.
    :param selector: *(Optional)* Selectors to highlight relevant nodes.
    '''
    params: T_JSON_DICT = dict()
    params['highlightConfig'] = highlight_config.to_json()
    if node_id is not None:
        params['nodeId'] = node_id.to_json()
    if backend_node_id is not None:
        params['backendNodeId'] = backend_node_id.to_json()
    if object_id is not None:
        params['objectId'] = object_id.to_json()
    if selector is not None:
        params['selector'] = selector
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.highlightNode',
        'params': params,
    }
    json = yield cmd_dict


def highlight_quad(
        quad: dom.Quad,
        color: typing.Optional[dom.RGBA] = None,
        outline_color: typing.Optional[dom.RGBA] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

    :param quad: Quad to highlight
    :param color: *(Optional)* The highlight fill color (default: transparent).
    :param outline_color: *(Optional)* The highlight outline color (default: transparent).
    '''
    params: T_JSON_DICT = dict()
    params['quad'] = quad.to_json()
    if color is not None:
        params['color'] = color.to_json()
    if outline_color is not None:
        params['outlineColor'] = outline_color.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.highlightQuad',
        'params': params,
    }
    json = yield cmd_dict


def highlight_rect(
        x: int,
        y: int,
        width: int,
        height: int,
        color: typing.Optional[dom.RGBA] = None,
        outline_color: typing.Optional[dom.RGBA] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

    :param x: X coordinate
    :param y: Y coordinate
    :param width: Rectangle width
    :param height: Rectangle height
    :param color: *(Optional)* The highlight fill color (default: transparent).
    :param outline_color: *(Optional)* The highlight outline color (default: transparent).
    '''
    params: T_JSON_DICT = dict()
    params['x'] = x
    params['y'] = y
    params['width'] = width
    params['height'] = height
    if color is not None:
        params['color'] = color.to_json()
    if outline_color is not None:
        params['outlineColor'] = outline_color.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.highlightRect',
        'params': params,
    }
    json = yield cmd_dict


def set_inspect_mode(
        mode: InspectMode,
        highlight_config: typing.Optional[HighlightConfig] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
    Backend then generates 'inspectNodeRequested' event upon element selection.

    :param mode: Set an inspection mode.
    :param highlight_config: *(Optional)* A descriptor for the highlight appearance of hovered-over nodes. May be omitted if ```enabled == false```.
    '''
    params: T_JSON_DICT = dict()
    params['mode'] = mode.to_json()
    if highlight_config is not None:
        params['highlightConfig'] = highlight_config.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setInspectMode',
        'params': params,
    }
    json = yield cmd_dict


def set_show_ad_highlights(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Highlights owner element of all frames detected to be ads.

    :param show: True for showing ad highlights
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowAdHighlights',
        'params': params,
    }
    json = yield cmd_dict


def set_paused_in_debugger_message(
        message: typing.Optional[str] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    :param message: *(Optional)* The message to display, also triggers resume and step over controls.
    '''
    params: T_JSON_DICT = dict()
    if message is not None:
        params['message'] = message
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setPausedInDebuggerMessage',
        'params': params,
    }
    json = yield cmd_dict


def set_show_debug_borders(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows debug borders on layers

    :param show: True for showing debug borders
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowDebugBorders',
        'params': params,
    }
    json = yield cmd_dict


def set_show_fps_counter(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows the FPS counter

    :param show: True for showing the FPS counter
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowFPSCounter',
        'params': params,
    }
    json = yield cmd_dict


def set_show_paint_rects(
        result: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows paint rectangles

    :param result: True for showing paint rectangles
    '''
    params: T_JSON_DICT = dict()
    params['result'] = result
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowPaintRects',
        'params': params,
    }
    json = yield cmd_dict


def set_show_layout_shift_regions(
        result: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows layout shift regions

    :param result: True for showing layout shift regions
    '''
    params: T_JSON_DICT = dict()
    params['result'] = result
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowLayoutShiftRegions',
        'params': params,
    }
    json = yield cmd_dict


def set_show_scroll_bottleneck_rects(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows scroll bottleneck rects

    :param show: True for showing scroll bottleneck rects
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowScrollBottleneckRects',
        'params': params,
    }
    json = yield cmd_dict


def set_show_hit_test_borders(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Requests that backend shows hit-test borders on layers

    :param show: True for showing hit-test borders
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowHitTestBorders',
        'params': params,
    }
    json = yield cmd_dict


def set_show_viewport_size_on_resize(
        show: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Paints viewport size upon main frame resize.

    :param show: Whether to paint size or not.
    '''
    params: T_JSON_DICT = dict()
    params['show'] = show
    cmd_dict: T_JSON_DICT = {
        'method': 'Overlay.setShowViewportSizeOnResize',
        'params': params,
    }
    json = yield cmd_dict


@event_class('Overlay.inspectNodeRequested')
@dataclass
class InspectNodeRequested:
    '''
    Fired when the node should be inspected. This happens after call to ``setInspectMode`` or when
    user manually inspects an element.
    '''
    #: Id of the node to inspect.
    backend_node_id: dom.BackendNodeId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> InspectNodeRequested:
        return cls(
            backend_node_id=dom.BackendNodeId.from_json(json['backendNodeId'])
        )


@event_class('Overlay.nodeHighlightRequested')
@dataclass
class NodeHighlightRequested:
    '''
    Fired when the node should be highlighted. This happens after call to ``setInspectMode``.
    '''
    node_id: dom.NodeId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodeHighlightRequested:
        return cls(
            node_id=dom.NodeId.from_json(json['nodeId'])
        )


@event_class('Overlay.screenshotRequested')
@dataclass
class ScreenshotRequested:
    '''
    Fired when user asks to capture screenshot of some area on the page.
    '''
    #: Viewport to capture, in device independent pixels (dip).
    viewport: page.Viewport

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ScreenshotRequested:
        return cls(
            viewport=page.Viewport.from_json(json['viewport'])
        )


@event_class('Overlay.inspectModeCanceled')
@dataclass
class InspectModeCanceled:
    '''
    Fired when user cancels the inspect mode.
    '''


    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> InspectModeCanceled:
        return cls(

        )
