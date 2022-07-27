var FoneCelMask = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 0 0000-0000' : '(00) 0 0000-0000';
  },
  celOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(FoneCelMask.apply({}, arguments), options);
      }
  };

var FoneMask = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 0000-0000' : '(00) 0000-0000';
  },
  foneOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(FoneMask.apply({}, arguments), options);
      }
  };

  var RamalMask = function (val) {
    return val.replace(/\D/g, '').length === 6 ? 'Ramal-0000' : 'Ramal-0000';
  },
  ramalOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(RamalMask.apply({}, arguments), options);
      }
  };


  django.jQuery(function(){

    django.jQuery('.mask-celular').mask(FoneCelMask, celOptions);

    django.jQuery('.mask-fone').mask(FoneMask, foneOptions);

    django.jQuery('.mask-ramal').mask(RamalMask, ramalOptions);

    django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});

    django.jQuery('.mask-cep').mask('00000-000');

    django.jQuery('#colaboradores_form').submit(function(){

        django.jQuery('#colaboradores_forms').find(":input[class*='mask-']").unmask();
        
    });


  });
  
 