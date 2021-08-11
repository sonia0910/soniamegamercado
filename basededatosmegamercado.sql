Create Database MegaMercado
go
use MegaMercado
go

CREATE Table login(
log_Usuario          Varchar(15) NOT NULL, 
Log_Contrasena       Numeric(15,0) NOT NULL,
Log_Ingreso          Varchar(2) NOT NULL
);

Insert Into login Values ('Sonia', '1234', '1');
Insert into login values ('Manuel', '456', '1');

SELECT * FROM login


CREATE Table Clientes(
Cli_Codigo			int identity(1,1) NOT NULL Primary key,
Cli_Direccion		Varchar(30) NOT NULL,
Cli_Nombres			Varchar(30) NOT NULL,
Cli_Apellidos		Varchar(30) NOT NULL,
Cli_RNC_Cedula		Numeric(11,0) NOT NULL,
Cli_Telefono		Numeric(10,0) NOT NULL,
Cli_Estatus			Varchar(1) NOT NULL
);

CREATE Table Proveedores(
Prov_Codigo			int identity(1,1) NOT NULL Primary key,
Prov_Direccion		varchar(50) NOT NULL,
Prov_Nombre			Varchar(15) NOT NULL,
Prov_Servicios		Varchar(40) NOT NULL,
Prov_Telefono		Numeric(9,0) NOT NULL,
Prov_Estatus		Varchar(1) NOT NULL
);


CREATE Table Productos(
Prod_Codigo			int identity(1,1) NOT NULL Primary key,
Prod_Nombre			varchar(50) NOT NULL,
Prod_PrecioVenta	Numeric(6,2) NOT NULL,
Prod_Proveedor      varchar(40) NOT NULL,
Prod_CostoUnidad	Numeric(5,2) NOT NULL,
Prod_ITBIS			Numeric(5,2) NOT NULL,
Prod_Estatus		Varchar(1) NOT NULL
);


CREATE Table Almacenes(
Alm_Producto			int NOT NULL References Productos (Prod_Codigo),
Alm_ValorInvertario		Numeric(6,2),
Alm_UnidadesDisponibles Numeric(6,0),
Primary Key(Alm_Producto)
);


CREATE Table Factura(
Fact_NoFactura		int identity(1,1) NOT NULL Primary Key,
Fact_Fecha			date NOT NULL,
Fact_Subtotal		Numeric(6,2) NOT NULL,
Fact_TotalITBIS		Numeric(5,2) NOT NULL,
Fact_Total			Numeric(7,2) NOT NULL,
Fact_Cliente		int NOT NULL Foreign Key References Clientes(Cli_Codigo)
);

CREATE Table DetalleFacturas(
Det_NoFactura		int NOT NULL Foreign Key References Factura(Fact_NoFactura),
Det_Producto		int NOT NULL Foreign Key References Productos(Prod_Codigo),
Det_Cantidad		Numeric(6,0) NOT NULL,
Det_NoAlmacen		int NOT NULL Foreign Key References Almacenes(Alm_Producto)
);

CREATE Table Pedidos(
Ped_NoPedido		int identity(1,1) NOT NULL Primary Key,
Ped_MontoTotal		Numeric(8,2) NOT NULL,
Ped_Proveedor		int NOT NULL Foreign Key References Proveedores(Prov_Codigo)
);

CREATE Table DetallePedido(
DetP_NoPedido		int NOT NULL Foreign Key References Pedidos(Ped_NoPedido),
DetP_Cantidad		Numeric(6,0) NOT NULL,
DetP_Producto		int NOT NULL Foreign Key References Productos(Prod_Codigo),
DetP_ProDescrp		Varchar(50) NOT NULL,
Ped_NoAlmacen		int NOT NULL Foreign Key References Almacenes(Alm_Producto)
);