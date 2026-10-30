import { useState, useEffect } from "react"

interface Post{
  id:number;
  title:string;
  body:string
}

const ClienteApi = () => {
   const [posts, setPosts]=useState<Post[]>([]);
   const [loading, setLoading] =useState<boolean>(true);

   //Busca os dados da api(pública) externa (promisse)

   useEffect(()=>{
     fetch("https://jsonplaceholder.typicode.com/posts?_limit=5")
     .then((res)=>res.json())
     .then((data:Post[])=>setPosts(data))
     .catch((error)=>console.log("erro ao acessar a api",error))
     .finally(()=>setLoading(false))
   },[])

  return (
    <div>
   <h2 className="text-xl font-semibold text-gray-700 mb-3">Api Externa</h2>

      {loading ? (
        <p className="text-gray-500 text-center">Carregando dados da API...</p>
      ) : (
         <ul className="space-y-3">
          {posts.map((post) => (
            <li key={post.id} className="border p-3 rounded bg-gray-50">
              <h3 className="font-bold text-gray-800 capitalize text-sm">{post.title}</h3>
              <p className="text-xs text-gray-600 mt-1">{post.body}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default ClienteApi
