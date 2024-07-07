import { useState } from "react";

const PhotoBooth = () => {
    const initial_photo = "https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/342ffe6b-b690-40d6-a788-714805262de0/%E5%A4%B4%E5%83%8F/w=828,quality=90,fit=scale-down";
    const [ photo, setPhoto ] = useState(initial_photo)
    
    async function SwitchPhoto() {
        const response = await fetch('http://127.0.0.1:5000/get_new_photo', {
            method: "GET",
        });
        newPhoto = response['url'];
        setPhoto(newPhoto);
    }
    
    return  ( 
        <>
            <div onClick={SwitchPhoto}>
                <img 
                    style={{ dispaly: 'flex', width: '50%' }} 
                    src={photo}>
                </img>
            </div>
        </>
    )
}

export default PhotoBooth;