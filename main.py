from repositorios import cliente_repositorio
from entidades import cliente

cliente = cliente.Cliente("João", 29)
repositorio_cliente = cliente_repositorio.ClienteRepositorio

repositorio_cliente.listar_clientes()
#cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente)
#cliente_repositorio.ClienteRepositorio.editar_cliente(3, cliente)
#cliente_repositorio.ClienteRepositorio.remover_cliente(6)

