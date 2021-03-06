"""
Export to Portable Document Format (PDF)

EXAMPLES::

    >>> from quill.exporter.svg import Svg
    >>> from tempfile import TemporaryFile
    >>> tmp = TemporaryFile(suffix='svg')
    >>> Svg(tmp).book(sample_book)
    >>> Svg(tmp).book(sample_book_xoj)
"""

import cairo

from quill.exporter.cairo_context import CairoContext


class Svg(CairoContext):
    """
    Exporter to PDF
    
    :param fileobj: a filename or a file-like object
    """
    
    def __init__(self, fileobj):
        """
        The Python constructor
        """
        height = 842   # A4 paper height in points
        width  = 595
        surface = cairo.SVGSurface(fileobj, width, height)
        context = cairo.Context(surface)
        super(Svg, self).__init__(context, width, height)

