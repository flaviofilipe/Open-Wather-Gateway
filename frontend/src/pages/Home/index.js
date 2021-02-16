import React from 'react'
import InputSearch from '../../components/InputSearch'
import CityWeatherCard from '../../components/CityWeatherCard'
import NotFoundText from '../../components/NotFoundText'

import { Container } from './style'

const Home = () => {
    return (
        <Container>
            <h1>WEATHER BUDDY</h1>
            <InputSearch />
            <NotFoundText />
            <CityWeatherCard />
        </Container>
    );
}


export default Home;
