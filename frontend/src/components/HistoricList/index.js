import React from 'react'
import { List } from './styles'
import CityWeatherCard from '../CityWeatherCard'

const DATA = {
    "city": "London",
    "description": "broken clouds",
    "temperature": "9ºC"
  }
const HistoricList = ({data}) => {
    if(data.length == 0){
        return <></>;
    }

    return (
        <List>
            {
                data.length > 0 && data.map(city => <CityWeatherCard key={city.id} data={city} />)
            }
        </List>
    )
}

export default HistoricList;