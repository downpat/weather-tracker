$(document).ready(function() {
  $('.draggable').draggable();
  $('#userCitiesPanel').droppable({
    drop: function( event, ui ) {
      window.location = ui.draggable.data('addcityurl');
    },
    over: function( event, ui ) {
      $(event.target).removeClass('panel-warning');
      $(event.target).addClass('panel-success');
    },
    out: function( event, ui ) {
      $(event.target).removeClass('panel-success');
      $(event.target).addClass('panel-warning');
    } 
  });
});
