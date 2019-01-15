/**
 * Created by Andres on 11/6/2017.
 */

is_nota_ok = function(value) {
        var lista_notas_admitidas = document.getElementById("listanotas").options;
        var arr = toArray(lista_notas_admitidas);
        return arr.indexOf(value) > -1;
    }


validAndConfirmExam = function(examen_id){
        var lista_notas = [];
        var formName = "form-nota" + examen_id;
        var modalName = "#Confirm" + examen_id;
        var formConfirmName = "#ConfirmExam" + examen_id;
        var nota_ok = true;
        forms = document.getElementsByName(formName)

        Array.prototype.forEach.call(forms, function(form) {
            lista_notas.push(form['nota'].value);
            nota_ok = nota_ok && is_nota_ok(form['nota'].value)
        });
        if(lista_notas.indexOf('PE') > -1 || lista_notas.length==0 || nota_ok == false){
            showAlert("Hay notas pendientes de carga!!");
            jQuery(modalName).modal('hide');
            return false;
        }else{
            jQuery(formConfirmName).submit();
            jQuery(modalName).modal('hide');
            return true
        }
    }

showAlert = function (alertText) {
    $('#alert_placeholder').html('<div class="alert"><a class="close" data-dismiss="alert">×</a><span>'+alertText+'</span></div>');
}

showMessage = function (msgtext) {
        var msg = document.getElementById("msg");
        msg = msgtext;
        msg.style.visibility = "visible";
    }

csrfSafeMethod = function(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

 efecto =  function(){
                     $('#fotocargando').hide();
                     $('#contenidoWeb').fadeIn(1500);
}



cursor_wait = function()
{
    // switch to cursor wait for the current element over
    var elements = $(':hover');
    if (elements.length)
    {
        // get the last element which is the one on top
        elements.last().addClass('cursor-wait');
    }
    // use .off() and a unique event name to avoid duplicates
    $('html').
    off('mouseover.cursorwait').
    on('mouseover.cursorwait', function(e)
    {
        // switch to cursor wait for all elements you'll be over
        $(e.target).addClass('cursor-wait');
    });
}

remove_cursor_wait = function()
{
    $('html').off('mouseover.cursorwait'); // remove event handler
    $('.cursor-wait').removeClass('cursor-wait'); // get back to default
}

ajaxSave = function(id){
    var formId = "#form-nota"+id;
    form = document.getElementById("form-nota"+id);

    var postData = {
        //'examen_alumno': $('input[name=examen_alumno]').val(),
        //'examen_alumno': $("+formId+"+" :input[name='examen_alumno']"),
        'examen_alumno': form['examen_alumno'].value,
        //'nota': $('input[name=nota]').val()
        'nota': form['nota'].value
    };


    cursor_wait();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    jQuery.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

    jQuery.ajax({
        type: "POST",
        url: "/examen_alumno/",
        data: postData,


        success: function(data)
        {
            if (data.result) {
                aid = data.aid;
                result = data.result;
                elementId = 'prGp' + aid;
                resultField = document.getElementById(elementId);
                resultField.innerHTML=result;
                $('html').off('mouseover.cursorwait'); // remove event handler
                $('.cursor-wait').removeClass('cursor-wait'); // get back to default
                }
            else {
                window.location.href = "/logout";
            }
        },
        error: function(xhr, statusText, err){
            window.location.href = "/logout";
        }
    });


    // simulation of a 3 sec ajax call
    //setTimeout(remove_cursor_wait, 5000);
}