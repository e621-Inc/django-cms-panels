var PanelInfo = ( function( $ ) {
    'use strict';

    // TODO make this usable for multiple panels

    var x;
    var y;
    var po;
    var pw;
    var ph;
    var mx;
    var my;

    var left;
    var top;
    var offset;

    var floor = Math.floor;
    var min   = Math.min;
    var max   = Math.max;

    var $body;
    var $fieldset;
    var $field_x;
    var $field_y;
    var $marker;
    var $panel;

    var $doc = $( document );

    $doc.ready( ready );

    function ready() {
        $body = $( 'body', $doc );
        $panel = $( '.panel-wrap' );

        if( $panel.length === 1 ) {
            $marker = $( '.panel-marker', $panel );
            $fieldset = $( '.coordinates' ).first();
            $field_x = $( '#' + $panel.data( 'field-x' ) );
            $field_y = $( '#' + $panel.data( 'field-y' ) );

            $panel.insertAfter( $fieldset.find( 'h2' ).first() );
            $marker.on( 'mousedown', drag_start );
        }

        function drag_start( e ) {
            offset = $marker.offset();

            $marker.off();
            $body.on( 'mousemove',  drag_over );
            $body.on( 'mouseup', drag_end );
            $panel.addClass( 'drag-over' );
        };

        function drag_over( e ) {
            po = $panel.offset();
            mx = e.clientX + $doc.scrollLeft();
            my = e.clientY + $doc.scrollTop();
            pw = $panel.width() + po.left;
            ph = $panel.height() + po.top;

            set_position( e );

            if( mx < po.left || mx > pw || my < po.top || my > ph ) {
                drag_end( e );
            }
        };

        function drag_end( e ) {
            $body.off();
            $panel.removeClass( 'drag-over' );
            $marker.off();
            $marker.on( 'mousedown', drag_start );
        };

        function set_position( e ) {
            left = floor( ( mx - po.left ) / $panel.width() * 10000 );
            top = floor( ( my - po.top ) / $panel.height() * 10000 );

            if( left < 0 ) {
                left = 0;
            } else if( mx > pw ) {
                left = 10000;
            }
            if( top < 0 ) {
                top = 0;
            } else if( my > ph ) {
                top: 10000;
            }

            $field_x.val( left );
            $field_y.val( top );

            $marker.css( {
                left: ( left / 100 ) + '%',
                top: ( top / 100 ) + '%'
            } );
        };
    };

} )( django.jQuery );
