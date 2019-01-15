#!/usr/bin/env python
# -*- coding: utf-8 -*-
from security.models.LeftMenu import LeftMenu

from guardian.shortcuts import get_objects_for_user
import collections
import json

class MenuService:
#    def __init__(self):
#        super(MenuService, self).__addModel__(LeftMenu())

    # Devuelve un jason con los items de menu permitidos a un usuario
    # ya ordenados y organizados por subcategorias
    # Ej:
    # {'menu':
    # [{'text':'Mis Materias','url':'/materias','icon':'fa fa-list-alt','codename':'mat_doce','childs':[]},
    # {'text':'Materias Coordinadas','url':'/materias','icon':'fa fa-list-alt','codename':'Ibal3bla','childs':[]},
    # {'text':'Reportes','url':'#','icon':'fa fa-fw fa-bar-chart','codename':'pepee','childs':[{'text':'Reporte de supervision','url':'/reportes/1','icon':'fa fa-circle-o','codename':'asdf','childs':[]},
    #                                                                                   {'text':'Reporte de avance','url':'/reportes/2','icon':'fa fa-circle-o','codename':'asdgf','childs':[]}]}]}
    def get_leftmenu_for_user(self, user):
        menu = get_objects_for_user(user, 'security.ver_item_menu', accept_global_perms=False)
        menu_dict= collections.OrderedDict()
        item_list = []
        added_items = []
        for item in menu:
            childs = self.get_childs_items(menu,item,added_items)
            url = item.url
            if item.perm :
                url = url + '/' + str(item.perm.pk)

            if childs:
                item_dict = {'text':item.text,'url':url,'icon':item.icon,'codename':item.codename,'childs':childs}
            else:
                item_dict = {'text': item.text, 'url': url, 'icon': item.icon, 'codename': item.codename}

            if item.id not in added_items:
                added_items.append(item.id)
                item_list.append(item_dict)
        menu_dict['menu']=item_list
        #menu_dict_s = stringify_keys(menu_dict)
        return json.dumps(menu_dict)

    #Recibe un todos los items de menu aplanados y un item en particular
    #Retorna un diccionario con aquellos item que son hijos del item dado
    def get_childs_items(self,menu, item, added_items):
        childs = []
        result = list(filter(lambda f: f.parent == item.id, menu))
        for item in result:
            url = item.url
            if item.perm:
                utl = url + '/' + str(item.perm.pk)
            item_dict = {'text':item.text,'url':url,'icon':item.icon,'codename':item.codename}
            childs.append(item_dict)
            added_items.append(item.id)
        return childs

    def create_item_menu(self, parent, text, url, icon,perm,codename):
        newItemMenu = LeftMenu()
        menu_parent = self.get_item_menu_by_id(parent)
        if menu_parent:
            this_parent = menu_parent.id
            this_depth = menu_parent.depth + 1
            this_path = menu_parent.path + str(menu_parent.id) + '/'
        else:
            this_parent = None
            this_depth = 0
            this_path = None


        try:
            newItemMenu = LeftMenu.objects.create( parent=this_parent,
                                                    depth=this_depth,
                                                    path=this_path,
                                                    text=text,
                                                    url=url,
                                                    icon=icon,
                                                    codename=codename,
                                                    perm=perm)
            newItemMenu.save()
        except Exception as e:
            e.args += (parent, url, text)
            e.message = "Error guardando registro"
            raise e
            return  e

        return newItemMenu

    def delete_item_menu(self,item_id):
        LeftMenu.objects.get(id=item_id).delete()

    def get_item_menu_by_id(self,id):
        ret = None
        try:
            ret = LeftMenu.objects.get(pk=id)
        finally:
            return ret