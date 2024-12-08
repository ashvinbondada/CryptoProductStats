import { useEffect, useState } from "react";
import ProductStats from "./components/ProductStats";

function App() {
  const [products, setProducts] = useState([]);

  const getProducts = async () => {
    const resp = await fetch(import.meta.env.VITE_API_URL + "/api/products/").then((res) => res.json()).catch((err) => console.log(err));
    setProducts(resp);
  }

  const handleDelete = async (id) => {
    await fetch(import.meta.env.VITE_API_URL + "/api/delete/" + id +"/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      },
    }).catch((err) => console.log(err)).then((res) => {
      if (res.status === 204) {
        getProducts()
      } else{
        alert("Error deleting product")
      }
    });
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch(import.meta.env.VITE_API_URL + "/api/submit/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: e.target.name.value,
        email: e.target.email.value,
        product: e.target.product.value
      })
    }).catch((err) => console.log(err)).then((res) => {
      if (res.status === 201) {
        getProducts()
      } else{
        alert("Error submitting form")
      }
    });
  }

  useEffect(() => {
    getProducts();
  }, [])

  return (
    <div className="flex flex-col w-screen h-screen">
        <h1 className="place-self-center text-5xl">Coinbase Asset Interest Form</h1>
        <div className="flex flex-col justify-center items-center">
          <form className="flex flex-col" onSubmit={handleSubmit}>
            <label htmlFor="name">Name:</label>
            <input className="p-2 w-max border-2 rounded-md border-black " type="text" id="name" name="name" placeholder="John Doe" />

            <label htmlFor="email">Email:</label>
            <input className="p-2 w-max border-2 rounded-md border-black" type="email" id="email" name="email" placeholder="johndoe@example.com" />

            <label htmlFor="product">Product:</label>
            <input className="p-2 w-max border-2 rounded-md border-black" type="text" id="product" name="product" placeholder="BTC-USD" />

            <button className="p-2 w-max border-2 rounded-md border-black place-self-center mt-2 bg-green-300 hover:bg-green-500" type="submit">Submit</button>
          </form>
        </div>
        <h1 className="place-self-center text-5xl">Product Cards</h1>
        <div className="grid grid-cols-4 justify-center">
          {products.length > 0 ? products.map((product) => {
            return <ProductStats key={product.id} props={product} handleDelete={handleDelete} />
          }) : <p className="pl-2 text-3xl ">No Products to Show</p>}
        </div>
    </div>
  );
}

export default App;