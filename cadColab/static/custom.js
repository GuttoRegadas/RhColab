var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 15 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };

  django.jQuery(function(){

    django.jQuery('.mask-celular').mask(SPMaskBehavior, spOptions);

    django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});

    django.jQuery('.mask-cep').mask('00000-000');

    django.jQuery('#colaboradores_form').submit(function(){

        django.jQuery('#colaboradores_forms').find(":input[class*='mask-']").unmask();

    });


  });
  
 