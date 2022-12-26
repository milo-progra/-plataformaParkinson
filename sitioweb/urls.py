from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app.views import EnviarCorreoView, HomeCorreosView, Registro_pacienteView, ReporteAudios,admin_enfermera, admin_familiar, admin_fonoaudiologo, admin_info_enfermera, admin_info_familiar, admin_info_fonoaudiologo,  admin_info_neurologo,  admin_neurologo, admin_paciente, admin_receta_paciente, agregar_bitacora, agregar_receta, apq11shimmer, apq3shimmer, aqpq5shimer, audio, automonitoreo_form, chart_animo, chart_automonitoreo, chart_vista_animo, chart_vista_automonitoreo, ddashimmer, ddpjitter, documento, documento_admin, editar_comentario, editar_comentario_bitacora, editar_comentario_intensidad, editar_receta, eliminar_receta, enf_pac, enfermera, enfermera_info_paciente, enfermera_paciente, enfermera_vista_info_paciente, estado_animo_form, f0, f0dev, f1, f2, f3, f4, familiar, familiar_info_paciente, familiar_paciente, fonoaudiologo, fonoaudiologo_vista_info_paciente, grafico_admin, grafico_audios_admin, grafico_cantidad_usuarios, grafico_enfermeras_comuna, grafico_fonoaudiologo_comuna, grafico_intensidad_admin, grafico_neurologo_comuna, grafico_pacientes_comuna, grafico_vocalizacion_admin, graficos, index, intensidad_paciente, localabsolutejitter, localdbshimer, localshimer, modificar_audio, modificar_audio_fonoaudiologo, neu_pac, neurologo, neurologo_info_paciente, neurologo_info_paciente_vista, neurologo_paciente, post_login, ppq5jitter, preregistro_admin, preregistros, rapjitter, receta,  registro_usuario, telegram, terapias_fono, vista_apq11shimmer, vista_apq3shimmer, vista_aqpq5shimer, vista_audio_paciente, vista_ddashimmer, vista_ddpjitter, vista_f0, vista_f0dev, vista_f1, vista_f2, vista_f3, vista_f4, vista_graficos, vista_intensidad, vista_localabsolutejitter, vista_localdbshimer, vista_localshimer, vista_ppq5jitter, vista_rapjitter, vista_vocalizacion, vocalizacion_paciente


urlpatterns = [
    
    path('admin/', admin.site.urls, name="admin"),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('api/', include('app.urls')),
    path('usuario/', include('usuario.urls')),
    path('paciente/', include('paciente.urls')),
    path('medicamento/', include('medicamento.urls')),
    path('fonoaudiologo/', include('fonoaudiologo.urls')),

    
    path('post_login/', post_login, name="post_login"),
    path('neurologo/', neurologo, name="neurologo"),
    path('neurologo_paciente/', neurologo_paciente, name="neurologo_paciente"),
    path('neurologo_info_paciente/<username_paciente_id>' , neurologo_info_paciente, name="neurologo_info_paciente"),
    path('neurologo_info_paciente_vista/<username_paciente_id>' , neurologo_info_paciente_vista, name="neurologo_info_paciente_vista"),
    path('receta/', receta, name="receta"),
    path('documento_admin/', documento_admin, name="documento_admin"),
    path('formularioemocion/', estado_animo_form, name="estado_animo_form"),
    path('automonitoreo_form/', automonitoreo_form, name="automonitoreo_form"),
    path('agregar_bitacora/<username_paciente_id>', agregar_bitacora, name="agregar_bitacora"),
    path('editar_comentario_bitacora/<id>', editar_comentario_bitacora, name="editar_comentario_bitacora"),
    path('editar_receta/<id_receta>', editar_receta, name="editar_receta"),
    path('eliminar_receta/<id_receta>', eliminar_receta, name="eliminar_receta"),
    path('agregar_receta/<username_paciente_id>', agregar_receta, name="agregar_receta"),
    path('chart_vista_animo/<username_paciente_id>', chart_vista_animo, name="chart_vista_animo"),
    path('chart_vista_automonitoreo/<username_paciente_id>', chart_vista_automonitoreo, name="chart_vista_automonitoreo"),
    path('familiar/', familiar, name="familiar"),
    path('familiar_paciente/', familiar_paciente, name="familiar_paciente"),
    path('chart_animo/<username_paciente_id>', chart_animo, name="chart_animo"),
    path('chart_automonitoreo/<username_paciente_id>', chart_automonitoreo, name="chart_automonitoreo"),
    path('enfermera/', enfermera, name="enfermera"),
    path('enfermera_paciente/', enfermera_paciente, name="enfermera_paciente"),
    path('enfermera_info_paciente/<username_paciente_id>' , enfermera_info_paciente, name="enfermera_info_paciente"),
    path('enfermera_vista_info_paciente/<username_paciente_id>' , enfermera_vista_info_paciente, name="enfermera_vista_info_paciente"),
    path('familiar_info_paciente/<username_paciente_id>' , familiar_info_paciente, name="familiar_info_paciente"),
    path('audio/<username_paciente_id>', audio, name="audio"),

    path('vocalizacion_paciente/<username_paciente_id>', vocalizacion_paciente, name="vocalizacion_paciente"),
    path('intensidad_paciente/<username_paciente_id>', intensidad_paciente, name="intensidad_paciente"),
    path('vista_audio_paciente/<username_paciente_id>', vista_audio_paciente, name="vista_audio_paciente"),
    path('vista_vocalizacion/<username_paciente_id>', vista_vocalizacion, name="vista_vocalizacion"),
    path('vista_intensidad/<username_paciente_id>', vista_intensidad, name="vista_intensidad"),
    path('fonoaudiologo/', fonoaudiologo, name="fonoaudiologo"),
    path('terapias_fono/', terapias_fono, name="terapias_fono"),

    
    path('fonoaudiologo_vista_info_paciente/<username_paciente_id>' , fonoaudiologo_vista_info_paciente, name="fonoaudiologo_vista_info_paciente"),
    path('f0/<username_paciente_id>', f0, name="f0"),
    path('f0dev/<username_paciente_id>', f0dev, name="f0dev"),
    path('localabsolutejitter/<username_paciente_id>', localabsolutejitter, name="localabsolutejitter"),
    path('rapjitter/<username_paciente_id>', rapjitter, name="rapjitter"),
    path('ppq5jitter/<username_paciente_id>', ppq5jitter, name="ppq5jitter"),
    path('ddpjitter/<username_paciente_id>', ddpjitter, name="ddpjitter"),
    path('localshimer/<username_paciente_id>', localshimer, name="localshimer"),
    path('localdbshimer/<username_paciente_id>', localdbshimer, name="localdbshimer"),
    path('apq3shimmer/<username_paciente_id>', apq3shimmer, name="apq3shimmer"),
    path('aqpq5shimer/<username_paciente_id>', aqpq5shimer, name="aqpq5shimer"),
    path('apq11shimmer/<username_paciente_id>', apq11shimmer, name="apq11shimmer"),
    path('ddashimmer/<username_paciente_id>', ddashimmer, name="ddashimmer"),
    path('f1/<username_paciente_id>', f1, name="f1"),
    path('f2/<username_paciente_id>', f2, name="f2"),
    path('f3/<username_paciente_id>', f3, name="f3"),
    path('f4/<username_paciente_id>', f4, name="f4"),
    path('graficos/<username_paciente_id>', graficos, name="graficos"),
    path('vista_f0/<username_paciente_id>', vista_f0, name="vista_f0"),
    path('vista_f0dev/<username_paciente_id>', vista_f0dev, name="vista_f0dev"),
    path('vista_localabsolutejitter/<username_paciente_id>', vista_localabsolutejitter, name="vista_localabsolutejitter"),
    path('vista_rapjitter/<username_paciente_id>', vista_rapjitter, name="vista_rapjitter"),
    path('vista_ppq5jitter/<username_paciente_id>', vista_ppq5jitter, name="vista_ppq5jitter"),
    path('vista_ddpjitter/<username_paciente_id>', vista_ddpjitter, name="vista_ddpjitter"),
    path('vista_localshimer/<username_paciente_id>', vista_localshimer, name="vista_localshimer"),
    path('vista_localdbshimer/<username_paciente_id>', vista_localdbshimer, name="vista_localdbshimer"),
    path('vista_apq3shimmer/<username_paciente_id>', vista_apq3shimmer, name="vista_apq3shimmer"),
    path('vista_aqpq5shimer/<username_paciente_id>', vista_aqpq5shimer, name="vista_aqpq5shimer"),
    path('vista_apq11shimmer/<username_paciente_id>', vista_apq11shimmer, name="vista_apq11shimmer"),
    path('vista_ddashimmer/<username_paciente_id>', vista_ddashimmer, name="vista_ddashimmer"),
    path('vista_f1/<username_paciente_id>', vista_f1, name="vista_f1"),
    path('vista_f2/<username_paciente_id>', vista_f2, name="vista_f2"),
    path('vista_f3/<username_paciente_id>', vista_f3, name="vista_f3"),
    path('vista_f4/<username_paciente_id>', vista_f4, name="vista_f4"),
    path('vista_graficos/<username_paciente_id>', vista_graficos, name="vista_graficos"),

    path('admin_paciente/', admin_paciente, name="admin_paciente"),
    path('admin_receta_paciente/<username_paciente_id>', admin_receta_paciente, name="admin_receta_paciente"),
    path('admin_familiar/', admin_familiar, name="admin_familiar"),
    path('admin_info_familiar/<username_familiar_id>', admin_info_familiar, name="admin_info_familiar"),
    path('admin_neurologo/', admin_neurologo, name="admin_neurologo"),
    path('admin_info_neurologo/<username_neurologo_id>', admin_info_neurologo, name="admin_info_neurologo"),
    path('admin_fonoaudiologo/', admin_fonoaudiologo, name="admin_fonoaudiologo"),
    path('grafico_admin/', grafico_admin, name="grafico_admin"),
    path('grafico_intensidad_admin/', grafico_intensidad_admin, name="grafico_intensidad_admin"),
    path('grafico_vocalizacion_admin/', grafico_vocalizacion_admin, name="grafico_vocalizacion_admin"),
    path('grafico_audios_admin/', grafico_audios_admin, name="grafico_audios_admin"),
    path('admin_info_fonoaudiologo/<username_fonoaudiologo_id>', admin_info_fonoaudiologo, name="admin_info_fonoaudiologo"),

    path('grafico_cantidad_usuarios/', grafico_cantidad_usuarios, name="grafico_cantidad_usuarios"),
    path('grafico_pacientes_comuna/', grafico_pacientes_comuna, name="grafico_pacientes_comuna"),
    path('grafico_neurologo_comuna/', grafico_neurologo_comuna, name="grafico_neurologo_comuna"),
    path('grafico_fonoaudiologo_comuna/', grafico_fonoaudiologo_comuna, name="grafico_fonoaudiologo_comuna"),
    path('grafico_enfermeras_comuna/', grafico_enfermeras_comuna, name="grafico_enfermeras_comuna"),

    path('admin_enfermera/', admin_enfermera, name="admin_enfermera"),
    path('admin_info_enfermera/<username_enfermera_id>', admin_info_enfermera, name="admin_info_enfermera"),


    path('documento/<username_paciente_id>', documento, name="documento"),

    
    
    

    path('telegram/<id>', telegram, name="telegram"),
    path('editar_comentario/<id>', editar_comentario, name="editar_comentario"),
    path('editar_comentario_intensidad/<id>', editar_comentario_intensidad, name="editar_comentario_intensidad"),
    path('editar_audio/<id_audio>/', modificar_audio, name='modificar_audio'),
    path('modificar_audio_fonoaudiologo/<id_audio>/', modificar_audio_fonoaudiologo, name='modificar_audio_fonoaudiologo'),
    path('reporte/', ReporteAudios.as_view(), name="reporte"),    

    path('', index,name="index"),
    

    path('enf_pac/<id>', enf_pac, name="enf_pac"),
    path('neu_pac/<id>', neu_pac, name="neu_pac"),

    path('registro_usuario/<id>', registro_usuario, name="registro_usuario"),
    path('registro_paciente/<id>', Registro_pacienteView.as_view(), name="registro_paciente"),
    
    path('preregistros/', preregistros, name="preregistros"),
    path('preregistro_admin/', preregistro_admin, name="preregistro_admin"),
    path('home_enviar_correo/', HomeCorreosView.as_view(), name='home_enviar_correo'),
    path('enviar_correo/<usuario>/', EnviarCorreoView.as_view(), name="enviar_correo")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
