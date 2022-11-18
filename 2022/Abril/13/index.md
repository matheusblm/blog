@Entity("users")
export class User{
@PrimaryGeneratedColumn("uuid")
id:string
@Column()
name: string
@column()
email: string;
@column()
password: string;
@column({default: false})
isAdmin: boolean;
@OneToMany(()=> Order, (order) => order.user)
orders: Order[]
}

@Entity('nome')
export class Nome {
@PrimaryGeneratedColumn("uuid")
id:string
@Column({length: 50})
name: string
@column({type: "float"})
price: number;
@OneToMany(()=> OrderProduct, ())
}

@Entity('order')
export class Order{
@PrimaryGeneratedColumn("uuid")
id: string;
@Column({default: new Date()})
order_date: Date
@ManyToOne(()=> User,(user) => users.orders)
user: User
@OneToMany(()=> OrderProducts, (OrderProducts)=> orderProducts.order)
orderProducts: OrderProduct[]
}

Tabela pivo

@Entity('order_product')
export class OrderProduct{
@PrimaryGeneratedColumn("uuid")
id: string;
@Column({default: new Date()})
sale_value: number;
@ManyToOne(()=> Product, (product)=>product.orderProducts )
@ManyToOne(()=> Order, (Order)=>order.orderProducts )
}

@Entity('Invoices')
export class Invoices{
@PrimaryGeneratedColumn("uuid")
id: string;
@Column({default: new Date()})
release_date: Date;
@Column({type: "uuid", unique: true})
invoice_number: string
@OnetoOne(()=> Oder, {nullable: true})
@JoinColumn()
order_id: string
}

demo do dia 4/5/2022
