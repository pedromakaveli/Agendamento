class Agendamento:
    def __init__(self):
        self.materiais = [
            {'id': '1', 'lab': 'civil', 'material': 'assds', 'dataDisponivel': ['1', '2', '3'], 'quantidade': 5},
            {'id': '2', 'lab': 'civil', 'material': 'ddd', 'dataDisponivel': ['1', '2', '3'], 'quantidade': 2}
        ]
        self.laboratorios = ['civil', 'd6']

    def exibirMateriais(self):
        for material in self.materiais:
            print(f'ID: {material["id"]} | Material: {material["material"]} | Quantidade: {material["quantidade"]}')

    def exibirLabs(self):
        for lab in self.laboratorios:
            return lab
        return None

    def buscar(self, idPassado=None, materialPassado=None, labPassado=None):
        if idPassado is not None:
            for material in self.materiais:
                if material['id'] == idPassado:
                    return material
            return None

        elif materialPassado is not None:
            for material in self.materiais:
                if material['material'] == materialPassado:
                    return material
            return None

        elif labPassado is not None:
            for material in self.materiais:
                if material['lab'] == labPassado:
                    return material
            return None

    def agendar(self):
        print(self.materiais)

if __name__ == '__main__':
    agd = Agendamento()
    menuInicial = input('[1] Agendar Material [2] Interromper: ')

    if menuInicial == '1':
        menuBusca = input('[1] Buscar material por laboratório [2] Exibir tudo [3] Sair: ')

        if menuBusca == '1':
            print('\nLaboratórios: ')
            print(agd.exibirLabs())
            labSelecionado = input('\nDigite o lab: ')
            materialEncontrado = agd.buscar(labPassado=labSelecionado)

            if materialEncontrado:
                print(f'Material encontrado: ID: {materialEncontrado["id"]} | Material: {materialEncontrado["material"]} | Local: {materialEncontrado["lab"]} | Quantidade: {materialEncontrado["quantidade"]}')
            else:
                print('Material não encontrado na base de dados!')

        if menuBusca == '2':
            print('\nMateriais:')
            agd.exibirMateriais()

            materialSelecionado = input('\nDigite a ID do produto ou o nome: ')
            materialEncontrado = None

            if materialSelecionado.isdigit():
                materialEncontrado = agd.buscar(idPassado=materialSelecionado)
            else:
                materialEncontrado = agd.buscar(materialPassado=materialSelecionado)


            if materialEncontrado:
                print(f'Material encontrado: ID: {materialEncontrado["id"]} | Material: {materialEncontrado["material"]} | Local: {materialEncontrado["lab"]} | Quantidade: {materialEncontrado["quantidade"]}')
            else:
                print('Material não encontrado na base de dados!')