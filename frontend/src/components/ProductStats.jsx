export default function ProductStats({props, handleDelete}) {
    return <div className="flex flex-col border-2 rounded-md border-black">
        <h1 className="text-3xl place-self-center">{props.product}</h1>
        <div className="flex flex-row place-content-evenly">
            <p className="text-2xl">Volume: {props.volume}</p>
            <p className="text-2xl">Last: {props.last}</p>
        </div>
        <div className="flex flex-row place-content-evenly">
            <p className="text-2xl">High: {props.high}</p>
            <p className="text-2xl">Low: {props.low}</p>
        </div>

        <button className="text-2xl border-2 rounded-md border-black bg-red-300 hover:bg-red-500" onClick={() => handleDelete(props.id)}>Delete</button>
    </div>
}