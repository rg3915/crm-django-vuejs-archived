USERS = [
    {
        'username': 'regis@email.com',
        'email': 'regis@email.com',
        'first_name': 'Regis',
        'last_name': 'Email',
        'group_name': 'simpleuser',
        'occupation': 'Desenvolvedor',
        'city': 'São Paulo',
        'uf': 'SP'
    },
    {
        'username': 'regis.santos.100@gmail.com',
        'email': 'regis.santos.100@gmail.com',
        'first_name': 'Regis',
        'last_name': 'Santos',
        'group_name': 'admin',
        'occupation': 'Desenvolvedor',
        'city': 'São Paulo',
        'uf': 'SP'
    },
]

OCCUPATION_LIST = (
    'Atendente',
    'Contador',
    'Desenvolvedor',
    'Gerente',
    'Secretária',
    'Vendedor',
)

COMPANIES = [
    {
        'name': 'Lorem Ipsum',
        'social_name': 'Lorem Ipsum Ltda',
        'email': 'lorem@email.com',
        'slug': 'lorem-ipsum',
        'address': 'Rua da Consolação',
        'address_number': '1000',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01302001',
        'cpf': '26696093095',
        'rg': '480728793',
        'cnh': '26405738956',
    },
    {
        'name': 'Blackjack Test',
        'social_name': 'Blackjack Test SA',
        'email': 'blackjack@email.com',
        'slug': 'blackjack',
        'address': 'Av. Brasil',
        'address_number': '4500',
        'complement': '',
        'district': 'Jardim Paulista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01400100',
        'cnpj': '63895690000104',
        'ie': '362012167511',
        'imun': '603103924168',
    },
    {
        'name': 'Bosch Test',
        'social_name': 'Bosch Test SA',
        'email': 'bosch@email.com',
        'slug': 'bosch',
        'address': 'Av. Paulista',
        'address_number': '2200',
        'complement': '5 andar',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310000',
        'cnpj': '61905039000142',
        'ie': '860233791246',
        'imun': '522291369401',
    },
    {
        'name': 'Everest Test',
        'social_name': 'Everest Test SA',
        'email': 'everest@email.com',
        'slug': 'everest',
        'address': 'Av. Paulista',
        'address_number': '3100',
        'complement': '5 andar',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310000',
        'cnpj': '61905039000143',
        'ie': '860233791247',
        'imun': '522291369402',
    },
    {
        'name': 'Diamond Test',
        'social_name': 'Diamond Test Ltda',
        'email': 'diamond@email.com',
        'slug': 'diamond',
        'address': 'Av. Paulista',
        'address_number': '450',
        'complement': '5 andar',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310000',
        'cnpj': '61905039000144',
        'ie': '860233791248',
        'imun': '522291369403',
    },
]


PROVIDERS = [
    {
        'name': 'Apple Test',
        'social_name': 'Apple Test SA',
        'email': 'apple@email.com',
        'slug': 'apple',
        'address': 'Av. Paulista',
        'address_number': '1500',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310001',
        'cnpj': '61905039000150',
        'ie': '860233791250',
        'imun': '522291369503',
    },
    {
        'name': 'Skyway Test',
        'social_name': 'Skyway Test SA',
        'email': 'skyway@email.com',
        'slug': 'skyway',
        'address': 'Av. Paulista',
        'address_number': '100',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01311000',
        'cnpj': '61905039000121',
        'ie': '860233791201',
        'imun': '522291369001',
    },
    {
        'name': 'Dante Test',
        'social_name': 'Dante Test ME',
        'email': 'dante@email.com',
        'slug': 'dante',
        'address': 'Av. Paulista',
        'address_number': '200',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01311000',
        'cnpj': '61905039000122',
        'ie': '860233791202',
        'imun': '522291369002',
    },
    {
        'name': 'Heroku Test',
        'social_name': 'Heroku Test SA',
        'email': 'heroku@email.com',
        'slug': 'heroku',
        'address': 'Av. Paulista',
        'address_number': '1',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01311000',
        'cnpj': '61905039000120',
        'ie': '860233791200',
        'imun': '522291369000',
    },
]

BANKS = [
    {
        'name': 'Banco do Brasil',
        'bank': '001',
    },
    {
        'name': 'Bradesco',
        'bank': '237',
    },
    {
        'name': 'Itaú',
        'bank': '341',
    },
    {
        'name': 'Santander',
        'bank': '033',
    }
]

TYPE_EXPENSES = (
    {
        'title': 'Almoço',
        'fixed': False,
    },
    {
        'title': 'Cartório',
        'fixed': False,
    },
    {
        'title': 'Diversos',
        'fixed': False,
    },
    {
        'title': 'Motoboy',
        'fixed': False,
    },
    {
        'title': 'Pagamento',
        'fixed': False,
    },
    {
        'title': 'Viagem',
        'fixed': False,
    },
    {
        'title': 'Alimentação',
        'fixed': False,
    },
    {
        'title': 'Correios',
        'fixed': False,
    },
    {
        'title': 'Correspondente',
        'fixed': False,
    },
    {
        'title': 'Cópias',
        'fixed': False,
    },
    {
        'title': 'Estacionamento',
        'fixed': False,
    },
    {
        'title': 'Estadia',
        'fixed': False,
    },
    {
        'title': 'Passagem Aérea',
        'fixed': False,
    },
    {
        'title': 'Tarifas Bancárias',
        'fixed': False,
    },
    {
        'title': 'Táxi',
        'fixed': False,
    },
)

EXPENSES = (
    {
        'description': 'Almoço com cliente',
        'type_expense': 'Almoço',
    },
    {
        'description': 'Alteração de contrato social',
        'type_expense': 'Cartório',
    },
    {
        'description': 'Cópia e autenticação',
        'type_expense': 'Cartório',
    },
    {
        'description': 'Entrega do Motoboy',
        'type_expense': 'Motoboy',
    },
    {
        'description': 'Motoboy',
        'type_expense': 'Motoboy',
    },
    {
        'description': 'Procuração em cartório',
        'type_expense': 'Cartório',
    },
    {
        'description': 'Reconhecimento de firma da procuração',
        'type_expense': 'Cartório',
    },
    {
        'description': 'Referente ao pedido',
        'type_expense': 'Diversos',
    },
    {
        'description': 'Viagem a trabalho',
        'type_expense': 'Viagem',
    },
    {
        'description': 'Viagem com cliente',
        'type_expense': 'Viagem',
    },
)


LOREM = 'lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip commodo consequat duis aute irure dolor reprehenderit voluptate velit esse cillum dolore fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim laborum'
