// Deleta objetos
$(document).on('click', '.object-delete', function() {
  let object = $(this).data('object')
  let url = $(this).data('url')
  $('#span-modal').text(object);
  $('#a-modal').attr("href", url);
});
