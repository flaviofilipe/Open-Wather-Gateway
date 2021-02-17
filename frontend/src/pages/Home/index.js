import React from 'react'
import InputSearch from '../../components/InputSearch'
import CityWeatherCard from '../../components/CityWeatherCard'
import { useState, useEffect } from 'react'
import NotFoundText from '../../components/NotFoundText'
import HistoricList from '../../components/HistoricList'

import api from '../../services/api'

import { Container } from './styles'

const Home = () => {
    const [city, setCity] = useState();
    const [data, setData] = useState({});
    const [historicData, setHistoricData] = useState({});
    const [showNotFoundText, setShowNotFoundText] = useState(false);
    const [showCityCard, setShowCityCard] = useState(false);

    useEffect(() => {
        if (city) {
            find_city_by_name();
        } else {
            setShowCityCard(false);
        }
    }, [city])

    const find_city_by_name = async () => {
        const response = await api.get("/weather/" + city)
            .then(response => {
                setData(response.data);
                setShowNotFoundText(false);
                setShowCityCard(true);
            })
            .catch((err) => {
                setShowCityCard(false);
                if (err.response.status === 404) {
                    setShowNotFoundText(true);
                }
            });
    }

    return (
        <Container>
            <h1>WEATHER BUDDY</h1>
            <InputSearch setCity={setCity} />
            <NotFoundText show={showNotFoundText} />
            <CityWeatherCard data={data} show={showCityCard} />
            <HistoricList data={historicData} />
        </Container>
    );
}


export default Home;
