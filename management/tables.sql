-- Database: `tcc`
--

-- --------------------------------------------------------

--
-- Table structure for table `alimento`
--

CREATE TABLE `alimento` (
  `ID` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `nome_alimento` varchar(40) NOT NULL,
  `quantidade_gramas` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `av_antopometrica`
--

CREATE TABLE `av_antopometrica` (
  `ID` int(11) NOT NULL,
  `id_func` int(11) NOT NULL,
  `peso` decimal(5,2) NOT NULL,
  `circunferencia_braco` decimal(4,2) NOT NULL,
  `circunferencia_adbomen` decimal(4,2) NOT NULL,
  `circunferencia_coxa` decimal(4,2) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `altura` decimal(3,2) NOT NULL,
  `IMC` decimal(2,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cidade`
--

CREATE TABLE `cidade` (
  `ID` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `consumo_alimentar`
--

CREATE TABLE `consumo_alimentar` (
  `ID` int(11) NOT NULL,
  `refrigerante` varchar(40) NOT NULL,
  `doces` varchar(40) NOT NULL,
  `frituras` varchar(40) NOT NULL,
  `fast_food` varchar(40) NOT NULL,
  `embutidos` varchar(40) NOT NULL,
  `enlatados` varchar(40) NOT NULL,
  `frutas` varchar(40) NOT NULL,
  `legumes` varchar(40) NOT NULL,
  `verdura` varchar(40) NOT NULL,
  `id_paciente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `diario_alimentar`
--

CREATE TABLE `diario_alimentar` (
  `ID` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `id_tipo_refeicao` int(11) DEFAULT NULL,
  `id_alimento` int(11) DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `visita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `dieta`
--

CREATE TABLE `dieta` (
  `ID` int(11) NOT NULL,
  `id_alimento` int(11) DEFAULT NULL,
  `gramas_alimento` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_tipo_refeicao` int(11) DEFAULT NULL,
  `data_elaboracao` date NOT NULL,
  `horario_refeicao` date NOT NULL,
  `numero_dieta` int(11) NOT NULL,
  `quantidade_calorias` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------



-- --------------------------------------------------------

--
-- Table structure for table `funcionario`
--

CREATE TABLE `funcionario` (
  `ID` int(11) NOT NULL,
  `id_tipo_func` int(11) DEFAULT NULL,
  `nome_completo` varchar(45) NOT NULL,
  `data_de_nascimento` date NOT NULL,
  `endereco` varchar(60) NOT NULL,
  `id_cidade` int(11) DEFAULT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;



-- --------------------------------------------------------

--
-- Table structure for table `historico_familiar`
--

CREATE TABLE `historico_familiar` ( FEITO
  `ID` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `doenca_cardiovascular` varchar(40) NOT NULL,
  `obesidade` varchar(40) NOT NULL,
  `hipertensao` varchar(40) NOT NULL,
  `cancer` varchar(40) NOT NULL,
  `diabetes` varchar(40) NOT NULL,
  `dislipidemias` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `historico_paciente`
--

CREATE TABLE `historico_paciente` (
  `ID` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `doenca_cardiovascular` varchar(40) NOT NULL,
  `obesidade` varchar(40) NOT NULL,
  `acido_urico` varchar(40) NOT NULL,
  `hipertensao` varchar(40) NOT NULL,
  `outros` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `info_nutricionais`
--

CREATE TABLE `info_nutricionais` (
  `ID` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_intolerancia` int(11) DEFAULT NULL,
  `preferencias_alimentar` varchar(255) NOT NULL,
  `id_diario_alimentar` int(11) DEFAULT NULL,
  `id_consumo_alimentar` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `intolerancia_alimentares`
--

CREATE TABLE `intolerancia_alimentares` (
  `ID` int(11) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Table structure for table `paciente`
--

CREATE TABLE `paciente` (
  `ID` int(11) NOT NULL,
  `CPF` int(14) NOT NULL,
  `nome_completo` varchar(255) NOT NULL,
  `data_de_nascimento` date NOT NULL,
  `genero` varchar(1) NOT NULL,
  `email` varchar(40) NOT NULL,
  `endereco` varchar(40) NOT NULL,
  `id_cidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------



--criar primeiro as tabelas sem dependencias--

-- Table structure for table `estado`
--

CREATE TABLE `estado` (
  `ID` int(11) NOT NULL,
  `nome_estado` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `refeicao`
--

CREATE TABLE `refeicao` (
  `ID` int(11) NOT NULL,
  `tipo_refeicao` varchar(40) NOT NULL,
  `horario_refeicao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `grupo`
--

CREATE TABLE `grupo` (
  `ID` int(11) NOT NULL,
  `nome_grupo` varchar(40) NOT NULL,
  `calorias` int(10) NOT NULL,
  `gramas_alimento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;