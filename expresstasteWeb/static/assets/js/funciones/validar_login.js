 function validar_acceso() {
    if($('#correo').val() == '') {
      $('#correo').css('border', '1px solid red');
    } else {
      $('#correo').css('border', '1px solid #ced4da')
    }
  }