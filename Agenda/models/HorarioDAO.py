import json
class HorarioDAO:__objetos= []
   
    @classmethod
    def inserir(cls, obj):cls.abrir()id=0
        for aux in cls.__objetos:
            if aux.get_id() > id: id= aux.get_id()obj.set_id(id
+
1