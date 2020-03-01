class CountError(TypeError):
    pass


class CheckCount:

    @staticmethod
    def check_val(val):
        if isinstance(val, str):
            raise CountError('Количество устройств должно быть целым числом')


class EquipmentWarehouse:
    __statistics = {'total_count': 0, 'in_departments': 0, 'Printer': 0, 'Scanner': 0, 'Copier': 0}
    __printers = {}
    __scanners = {}
    __copiers = {}
    __in_departments = {}
    _stat = None

    def __str__(self):
        return f'**********************************************************************************************\n' \
               f'Total statistics:\n{", ".join([f"{key} - {val}" for key, val in self.__statistics.items()])}' \
               f'\nPrinters: {self.__printers}\nScanners: {self.__scanners}\nCopiers: {self.__copiers}\n' \
               f'In departments:\n{", ".join([f"{key} - {val}" for key, val in self.__in_departments.items()])}\n' \
               f'**********************************************************************************************'

    @classmethod
    def add_equip(cls, obj, val):
        key = obj.__class__.__name__
        try:
            CheckCount.check_val(val)
        except CountError as e:
            print(f'Error placing {obj.app_model} in stock - {e}')
        else:
            if key in cls.__statistics.keys():
                cls.__statistics[key] += val
                cls.__statistics['total_count'] += val
                if key == 'Printer':
                    cls._stat = cls.__printers
                elif key == 'Scanner':
                    cls._stat = cls.__scanners
                elif key == 'Copier':
                    cls._stat = cls.__copiers
                if obj.app_model in cls._stat:
                    cls._stat[obj.app_model] += val
                else:
                    cls._stat.setdefault(obj.app_model, val)
            print(f'------------------------------------------------------------------------------------\n'
                  f'{key} - {obj.app_model} is located in the warehouse \n{cls.__statistics}\n'
                  f'------------------------------------------------------------------------------------')

    @classmethod
    def issuance_equip(cls, obj, val, dep_name):
        key = obj.__class__.__name__
        try:
            CheckCount.check_val(val)
        except CountError as e:
            print(f'Error issuance {obj.app_model} in department - {e}')
        else:
            if key in cls.__statistics.keys():
                cls.__statistics[key] -= val
                cls.__statistics['in_departments'] += val
                if dep_name in cls.__in_departments:
                    if obj.app_model in cls.__in_departments[dep_name]:
                        cls.__in_departments[dep_name][obj.app_model] += val
                    else:
                        cls.__in_departments[dep_name].update({obj.app_model: val})
                else:
                    cls.__in_departments.update({dep_name: {obj.app_model: val}})
                if key == 'Printer':
                    cls._stat = cls.__printers
                elif key == 'Scanner':
                    cls._stat = cls.__scanners
                elif key == 'Copier':
                    cls._stat = cls.__copiers
                if obj.app_model in cls._stat:
                    cls._stat[obj.app_model] -= val
            print(f'-------------------------------------------------------------------------------------\n'
                  f'{key} - {obj.app_model} was issued to the department {dep_name}\n{cls.__statistics}\n'
                  f'-------------------------------------------------------------------------------------')


class OfficeAppliances:

    def __init__(self, app_model, price, **kwargs):
        self.app_model = app_model
        self.price = price
        self.other = {key: val for key, val in kwargs.items()}


class Printer(OfficeAppliances):
    def __init__(self, app_model, price, print_type, count, resource, color=False, **kwargs):
        super().__init__(app_model, price, **kwargs)
        self.print_type = print_type
        self.color = color
        self.cartridge_count = count
        self.cartridge_resource = resource


class Scanner(OfficeAppliances):
    def __init__(self, app_model, price, depth, scan_type, optic_dens, **kwargs):
        super().__init__(app_model, price, **kwargs)
        self.bit_depth = depth
        self.scan_type = scan_type
        self.optical_density = optic_dens


class Copier(OfficeAppliances):
    def __init__(self, app_model, price, copy_count, bilateral=False, scaling=False, **kwargs):
        super().__init__(app_model, price, **kwargs)
        self.bilateral = bilateral
        self.copy_count_for_cycle = copy_count
        self.scaling = scaling


if __name__ == '__main__':
    my_warehouse = EquipmentWarehouse()

    printer_1 = Printer('Xerox-4455', 12500, 'laser', 1, 10000)
    printer_2 = Printer('Samsung ML-4325', 24300, 'laser', 4, 10000, color=True, paper_format='A4')
    scanner_1 = Scanner('Epson 1333', 3200, 600, 'flatbed', 4)
    copier_1 = Copier('HP4229e', 18000, 120, bilateral=True)

    print(printer_1.__dict__)
    print(printer_2.__dict__)

    my_warehouse.add_equip(printer_1, 5)
    my_warehouse.add_equip(printer_1, '5')
    my_warehouse.add_equip(printer_2, 7)
    my_warehouse.add_equip(scanner_1, 3)
    my_warehouse.add_equip(copier_1, 4)

    print(my_warehouse)

    my_warehouse.issuance_equip(printer_1, 2, 'personnel_department')
    my_warehouse.issuance_equip(printer_1, 1, 'personnel_department')
    my_warehouse.issuance_equip(scanner_1, 1, 'technical_department')
    my_warehouse.issuance_equip(copier_1, 2, 'technical_department')
    print(my_warehouse)
