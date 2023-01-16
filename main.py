from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
import webbrowser
import dimensionamento


sm = ScreenManager()
resultado = str('.....')


class RegisterScreen(Screen):
    pass

class PrincipalScreen(Screen):
    pass

class DimensionamentoScreen(Screen):
    pass

class RiscosScreen(Screen):
    pass

class QuimicosScreen(Screen):
    string= """ O risco químico é a probabilidade de sofrer agravo a que determinado indivíduo está exposto ao manipular produtos químicos que podem causar-lhe danos físicos ou prejudicar lhe a saúde.

Consideram-se agentes de risco químico as substâncias, compostos ou produtos que possam penetrar no organismo do trabalhador principalmente pela via respiratória, nas formas de poeiras, fumos gases, neblinas, nevoas ou vapores, ou pela natureza da atividade, de exposição, possam ter contato ou ser absorvido pelo organismo através da pele ou por ingestão.



Os agentes químicos podem apresentar-se nos diversos estados físicos nos ambientes de trabalho, e durante os processos podem sofrer mudanças. A possibilidade de uma substância química entrar no organismo está associado ao  seu estado físico.



Danos físicos e danos à saúde
Os danos físicos relacionados à exposição química incluem, desde irritação na pele e olhos, passando por queimaduras leves, indo até aqueles de maior severidade, causados por incêndio ou explosão. Os danos à saúde podem advir de exposição de curta e/ou longa duração, relacionadas ao contato de produtos químicos tóxicos com a pele e olhos, bem como a inalação de seus vapores, resultando em doenças respiratórias crônicas, doenças do sistema nervoso, doenças nos rins e fígado, e até mesmo alguns tipos de câncer.

Os principais efeitos causados pelas substâncias químicas:
Efeitos irritantes: são causados, por exemplo, por ácido clorídrico, ácido sulfúrico, amônia, soda cáustica, cloro, que provocam irritação das vias aéreas superiores.

Efeitos asfixiantes: são causados, por exemplo, por gases como hidrogênio, nitrogênio, hélio, metano, acetileno, dióxido de carbono, monóxido de carbono e outros causam dor de cabeça, náuseas, sonolência, convulsões, coma e até a morte.

Efeitos anestésicos: a maioria dos solventes orgânicos assim como o butano, propano, aldeídos, acetona, cloreto de carbono, benzeno, xileno, alcoóis, tolueno, tem ação depressiva sobre o sistema nervoso central, provocando danos aos diversos órgãos. O benzeno especialmente é responsável por danos ao sistema formador do sangue.

Poeiras minerais: provêm de diversos minerais, como sílica, asbesto, carvão mineral, e provocam silicose (quartzo), asbestose (asbesto), pneumoconioses (ex.: carvão mineral, minerais em geral).

Poeiras vegetais: são produzidas pelo tratamento industrial, por exemplo, de bagaço de cana-de-açúcar e de algodão, que causam bagaçose e bissinose, respectivamente.

Poeiras alcalinas: provêm em especial do calcário, causando doenças pulmonares obstrutivas crônicas, como enfisema pulmonar.

Poeiras incômodas: podem interagir com outros agentes agressivos presentes no ambiente de trabalho, tornando-os mais nocivos à saúde.

Fumos metálicos: provenientes do uso industrial de metais, como chumbo, manganês, ferro, etc., causando doença pulmonar obstrutiva crônica, febre de fumos metálicos, intoxicações específicas, de acordo com o metal.

"""

class FisicosScreen(Screen):
    string = """Quais são os riscos físicos nas empresas?
Ruídos
Ruídos são riscos físicos porque são provenientes de oscilações nas vibrações que se propagam pelo ar.

Dependendo de sua intensidade, podem causar problemas de audição temporária ou até permanente.

São muito comuns na construção civil e na indústria, mas também estão presentes no trânsito, nos telefonemas constantes e até mesmo no comércio, dependendo da agitação e do tom de voz das pessoas.

Para prevenir riscos relacionados ao ruído, as seguintes medidas podem ser adotadas:

Uso de EPIs;
Isolamento acústico do local;
Controle do tempo de exposição;
Revezamento de equipes;
Troca de equipamentos por outros mais silenciosos.
 

Vibrações
As vibrações são um tipo de risco físico comum, proveniente das oscilações de um corpo, equipamento ou superfície em contato com o trabalhador.

Dividem-se em duas categorias, sendo as localizadas, como o uso de motosserras, britadeiras e furadeiras, e as de corpo inteiro, como dirigir caminhões e tratores.

Esse tipo de risco pode causar desde formigamentos e dores musculares até problemas de coluna e osteoporose.

Para prevenir, as sugestões são:

Cuidados com a postura;
Revezamento de funcionários;
Intervalos para descanso;
Adequação do maquinário para reduzir as vibrações.
Infelizmente, não há nada que se possa usar para eliminar o risco. Então, a prevenção fica por conta da dosagem.

 

Temperatura
Tanto temperaturas frias quanto quentes são danosas à saúde do trabalhador, e entram na categoria dos riscos físicos.

Cozinhas industriais, trabalho a céu aberto e siderúrgicas são exemplos de riscos de altas temperaturas.

Já no risco de frio, encontramos os frigoríficos, o trabalho portuário com cargas congeladas e açougues.

Para prevenir contra o calor:

Utilize EPIs;
Isole a fonte de calor;
Mantenha a ventilação do ambiente;
Use protetor solar;
Faça intervalos quando o sol estiver forte.
Para prevenir contra o frio:

Use EPIs;
Faça intervalos;
Monitore a temperatura do ambiente.
 

Umidade
Este risco físico é menos comum, mas não menos perigoso. A umidade pode provocar quedas, deslizamentos, doenças respiratórias e problemas de pele.

Construções em locais alagados, lavanderias, lava jatos e frigoríficos são lugares onde o risco de umidade é comumente encontrado.

Há o risco de quedas e problemas respiratórios, e ainda o de contato com umidade contaminada, que já caracteriza um risco químico ou biológico, dependendo da natureza da contaminação.

As seguintes medidas podem ser tomadas para se prevenir:

Uso de botas de borracha, luvas e outros EPIs;
Ralos para escoamento de água;
Barreiras de contenção para evitar deslizamentos.
 

Pressão
A pressão pode ser dividida entre hiperbárica e hipobárica. A pressão hiperbárica é a mais perigosa, caracterizada por um ambiente que tem a pressão maior do que a pressão atmosférica.

Os mergulhadores são os profissionais mais expostos a esse tipo de risco físico.

Ela pode causar desde dificuldade para respirar até paralisias e morte.

Quando o mergulhador está embaixo d’água, os tecidos do corpo absorvem o nitrogênio do gás comprimido. Se o profissional subir de volta à superfície rápido demais, o nitrogênio entra na corrente sanguínea, envenenando o sangue e causando a morte.

Por isso existe o processo de descompressão, onde o profissional deve retornar lentamente à superfície.

Já a pressão hipobárica é quando o trabalhador está em um ambiente com pressão menor do que a pressão atmosférica.

Isso é mais comum para quem trabalha em grandes alturas.

Os riscos são o rompimento dos tímpanos, o rompimento de pequenos vasos sanguíneos, sangramentos nasais ou pelos ouvidos, dores de cabeça, náuseas e desmaios.

A prevenção, neste caso, deve ser feita com ingestão de muita água e uso de bombas de oxigênio.

 

Radiações
As radiações também podem ser divididas em duas, sendo as ionizantes (provenientes de materiais radioativos) e as não ionizantes (radiações simples, como os raios UV).

A radiação ionizante é capaz de modificar os átomos do corpo, podendo causar câncer em quem estiver em exposição direta.

Além disso, também pode causar doenças de pele, osteoporose e doenças hereditárias nas futuras gerações, se a pessoa vier a ter filhos ou netos.

Máquinas de Raio X são os aparelhos mais comuns que oferecem esse tipo de risco, e ele também pode ser encontrado em usinas nucleares e laboratórios.

As medidas de prevenção são:

Redução do tempo de exposição;
Uso de avental plumbífero (feito com chumbo para conter a radiação);
Barreiras físicas entre o profissional e a fonte;
Armazenamento e descarte adequados.
Já a radiação não ionizante pode ser encontrada nos raios solares, nas operações de solda e nas siderúrgicas.

Os riscos são lesões nos olhos e na pele, catarata e câncer.

As principais medidas preventivas são:

Uso de EPIs;
Uso de chapéus;
Roupas de manga longa;
Uso de protetor solar.
 

Como preparar minha empresa?
Para garantir a máxima proteção contra os riscos físicos, é necessário realizar um estudo de higiene ocupacional.

A higiene ocupacional é o que determina todos os riscos presentes no ambiente de trabalho para que você saiba quais são e como lidar com eles.

Ela também classifica esses riscos de acordo com sua gravidade.

Entenda melhor como funciona a higiene ocupacional e prepare sua empresa para evitar acidentes e doenças ocupacionais.

"""

class BiologicosScreen(Screen):
    string = """São diversos os riscos no qual um trabalhador está exposto diariamente em seu ambiente de trabalho, os riscos biológicos também não ficam de fora e são um dos principais fatores no qual o trabalhador e empregador devem sempre ficar em constante alerta.

Riscos biológicos são toda e qualquer probabilidade da exposição ocupacional a algum tipo de agente biológico. Sendo os mesmos riscos ambientais assim como os riscos químicos e físicos.

SÃO CONHECIDOS COMO PRINCIPAIS AGENTES BIOLÓGICOS:
— Microrganismos (bactérias, fungos e vírus do HIV), parasitas internos (vermes), parasitas externos (sarna, piolho e berne) e protozoários.


O QUE OS AGENTES BIOLÓGICOS PODEM CAUSAR NO TRABALHADOR?
— Bactérias: as bactérias podem causar desde uma leve pneumonia, infecção alimentar e até mesmo em casos graves uma tuberculose.

— Vírus: Os vírus podem causar no ambiente de trabalho desde pequenas gripes e resfriados, hepatite, sarampo, caxumba e em casos mais graves HIV.

— Fungos: Os fungos existentes no ambiente de trabalho podem ser causadores de micoses, candidíase, dentre outros tipos.

— Protozoários: Os protozoários existentes no ambiente de trabalho podem causar desde giardíase até mesmo doença de chagas.

Baixar eBook SST: GRO - Guia para o PGR e Matriz de Riscos

 

Vale ressaltar que os riscos biológicos existentes no ambiente de trabalho, estão presentes nos seguintes ambientes:

— Laboratórios

— Industria alimentícia

— Hospitais

— Abatedouro

— Agricultura

 

Porém, de modo geral, os ambientes mais conhecidos por ofertarem um maior potencial de riscos biológicos são os hospitais e serviços relacionados a saúde.


CLASSIFICAÇÃO DOS AGENTES BIOLÓGICOS
 

Os agentes biológicos de modo geral, podem ser classificados de acordo com o risco que o mesmo apresenta para a saúde de um colaborador.
A Classificação do mesmo atribui aos agentes biológicos uma divisão em classes de riscos, sendo eles 1, 2, 3 e 4.


— Classe de Risco 1:  A classe de risco 1 são agentes biológicos que venham oferecem um nível baixo de risco para os trabalhos e para um grupo dos mesmos. Oferece para trabalhadores individuais um risco muito baixo de propagação. Não há nenhuma comprovação de que seja capaz de transmitir doenças a pessoas ou animais saudáveis nessa classe de risco.


— Classe de Risco 2: Na classe de risco 2 os agentes biológicos já apresentam um nível de risco mais moderado para o trabalhador e risco fraco para trabalhos executados em grupo. A classe de risco 2 pode vir a desencadear doenças em pessoas e animais, porém há tratamentos e medidas preventivas. Ou seja na classe de risco 2 o nível de risco individual é moderado e risco de propagação baixo (por ex: herpes).


— Classe de Risco 3: Na classe de risco 3 os agentes biológicos apresentam um grau de risco maior sendo considerado elevado para a saúde do trabalhador e risco moderado para trabalhos de origem coletiva. A classe de risco 3 pode desenvolver doenças graves tanto em pessoa quando em animais. No caso da classe de risco 3 nem sempre há uma forma de tratamento funcional. Ou seja na classe de risco 3 nível de risco individual é elevado e o nível se risco de propagação moderado (por ex: febre amarela, HIV).


— Classe de Risco 4: Na classe de risco 4 os agentes biológicos são de alta periculosidade, apresentando nesse caso um grau de risco mais elevado para o trabalhador individual e coletivo. Podendo nesse caso vir a desenvolver doenças com um alto grau de complexidade tanto em pessoas quanto em animais. Não há forma de tratamento. Ou seja, na classe de risco 4

O nível de risco individual é elevado e o nível de risco de propagação elevado (por ex: vírus de febres hemorrágicas, ebola).

IDENTIFICANDO OS RISCOS BIOLÓGICOS
Para fazer o reconhecimento dos riscos biológicos existentes no ambiente de trabalho, deverá ser levado sempre em consideração os agentes biológicos mais frequentes.

O local no qual os trabalhadores exercem as atividades de trabalho é de suma importância para que sejam incentivados riscos em potencial, alguns agentes biológicos podem ser mais presentes em algumas regiões do em quem outras.

Logo, aquele agente biológico que apresenta um maior índice devera sempre ser levado em conta na avaliação.

Os agentes biológicos podem ser os principais causadores de doenças de pequeno ou grande complexidade, podendo as mesmas serem ou não contagiosas ou graves.

Podendo também causar sérios danos a integridade física dos trabalhadores levando até mesmo a um afastamento do ambiente de trabalho."""

class ErgonomicosScreen(Screen):
    string = """Segundo o engenheiro e ergonomista Itiro Iida, a ergonomia é o estudo da adaptação do trabalho ao homem. O trabalho aqui tem uma acepção bastante ampla, abrangendo não apenas aqueles executados com máquinas e equipamentos, utilizados para transformar os materiais, mas também os aspectos organizacionais. A ergonomia tem uma visão ampla, abrangendo atividades de planejamento e projeto, que ocorrem antes do trabalho ser realizado, e aqueles de controle e avaliação, que ocorrem durante e após esse.

Em uma situação ideal, a ergonomia deve ser aplicada desde as etapas iniciais do projeto de uma máquina, sistema, ambiente ou local de trabalho. Essas devem sempre incluir o ser humano como um de seus componentes. Assim, as características desse operador devem ser consideradas juntamente com as características ou restrições das partes mecânicas, sistêmicas ou ambientais, para se ajustarem mutuamente umas às outras.

O conceito de ergonomia realmente é bastante abrangente, sendo hoje aplicável na indústria, comércio, setor de serviços e até mesmo na vida do cidadão comum. Detectamos os riscos ergonômicos, a partir da AET – Análise Ergonômica do Trabalho, prevista na Norma Regulamentadora n° 17 (NR 17) do Ministério do Trabalho e Emprego. Existem riscos ergonômicos que podemos dizer que são mais comuns nas empresas, principalmente no ambiente industrial, dentre os quais citamos logo abaixo:

1 – Trabalho repetitivo:

É um dos principais fatores de origem dos distúrbios dos membros superiores. Segundo o ergonomista Hudson Couto, referência nacional no tema de ergonomia, quando o assunto é a análise individual do fator repetitividade, as pesquisas indicam que os ciclos curtos se tornam um risco muito significativo quando, em decorrência deles, há acima de 6 mil repetições por turno de trabalho. É esperado que trabalhadores submetidos a essa situação, sem pausas ou outros mecanismos de regulação e que estejam apresentando o problema, com o decorrer do tempo, na função, venham apresentar algum distúrbio ou lesão. Entre 3 e 6 mil repetições por turno, a incidência de distúrbios e lesões ocorre entre 12 e 20% dos expostos.

Abaixo de 3 mil, ocorre alguma incidência, e, abaixo 1 mil, a exposição é considerada segura. O trabalho repetitivo é muito comum em fábricas com linhas de montagem, locais de inspeção de itens de produção (geralmente no setor de qualidade), trabalhos de lixamento e polimento de peças, atividades de costura e corte (principalmente na indústria de vestuário), entre outras.

2 – Levantamento e transporte manual de cargas (principalmente superiores a 25kg):

O transporte de pesos provoca uma sobrecarga fisiológica nos músculos da coluna e dos membros inferiores. O manuseio de cargas é responsável por grande parte dos traumas musculares entre os trabalhadores. De acordo com o ergonomista inglês Robert Bridger, aproximadamente 60% dos problemas musculares são causados por levantamento de cargas e 20% puxando-as ou empurrando-as.

Isso ocorre principalmente devido à grande variação individual das capacidades físicas, treinamentos insuficientes e frequentes substituições de trabalhadores. Esforços muito intensos feitos com os membros superiores são de alto potencial lesivo, principalmente porque, para eles, as pausas ou rodízios são mecanismos ineficazes de compensação.  Esses riscos são muito comuns em trabalhadores das áreas de expedição, almoxarifados, carregadores de caminhões ou outros que precisam transportar materiais na produção, sem uso de equipamentos (carrinhos ou paleteiras).

3 – Esforços estáticos e posturas estáticas (má postura):

Normalmente, os trabalhadores assumem posturas inadequadas devido ao projeto deficiente das máquinas, equipamentos, postos de trabalho e às exigências da tarefa. As situações principais em que a má postura pode produzir consequências danosas são:

Trabalho estático que envolva uma postura parada por longos períodos;
Trabalhos que exigem posturas desfavoráveis, como o tronco inclinado e torcido;
Pescoço excessivamente flexionado;
Braços elevados acima do nível dos ombros;
Braços ou antebraços suspensos.
Essas situações podem ocasionar falta de oxigênio nos tecidos, dor e tendência à lesão por acúmulo de ácido láctico nos tecidos.

Podemos citar entre os expostos a estas situações: trabalhos com estoques de mercadorias elevadas, atividades dos mecânicos de manutenção, linhas de montagem de alta precisão, trabalhos administrativos com uso de computador ou notebook, eletricistas, soldadores e outros.

4 – Fatores de organização do trabalho:

As ocorrências mais frequentes são: carga de trabalho excessiva, insuficiência de pessoal, mão de obra insuficientemente preparada, prazos assumidos sem a devida consideração sobre a capacidade de mão de obra, urgências e emergências, retrabalho e retrocesso, falta de material para completar o trabalho, falta de manutenção, problemas com qualidade do material, exigindo esforço extra dos trabalhadores. Tudo isso gera sobrecarga no trabalho além de tensional, que se apresenta sob a forma de horas extras excessivas, dobras de turno, trabalhos aos sábados, domingos e feriados. Esses fatores eliminam os tempos de recuperação da fadiga.

Conforme afirma o ergonomista Hudson Couto, a pressão excessiva sobre os trabalhadores e outros fatores psicossociais fazem com que o trabalhador fique tenso, prejudicando a recuperação das estruturas. Quando uma pessoa está excessivamente tensa, a tensão interna dos músculos prejudica a circulação do sangue e um dos principais sintomas é a dor nos músculos do pescoço e dos ombros, também denominada “dor em cabide” explicada pelo acúmulo de ácido láctico.

Os riscos psicossociais decorrem de deficiências na organização e gestão do trabalho bem como de um contexto social de trabalho problemático, podendo ter efeitos negativos a nível psicológico, físico e social, tais como estresse relacionado com o trabalho, esgotamento ou depressão. Quaisquer ambientes de trabalho podem apresentar estes fatores de riscos.

5 – Fatores ambientais:

Uma grande fonte de tensão no trabalho são as condições ambientais desfavoráveis, como excesso de calor ou frio, ruídos, vibrações, agentes químicos nocivos e iluminação. Esses fatores causam desconforto, aumentam o risco de acidentes e podem provocar danos consideráveis à saúde.

Para cada uma dessas variáveis ambientais, há certas características que são mais prejudiciais ao trabalho. Tanto o frio quanto o calor comprometem muito a capacidade produtiva, como também ambientes ruidosos, acima de 90dB, provocando reações fisiológicas prejudiciais ao organismo, aumentando o estresse e a fadiga.

A vibração direta sobre o corpo humano pode provocar efeitos fisiológicos e psicológicos, como perda de equilíbrio, falta de concentração e visão turva, diminuindo a acuidade visual.

Os agentes químicos nocivos à saúde atingem o organismo por via da ingestão, contato com a pele e inalação. Alguns agentes bastante encontrados nas indústrias são: monóxido de carbono, solventes, metais pesados, agrotóxicos, sílica e gases.

Um ambiente de trabalho com iluminação inadequada pode provocar ao trabalhador: queda de rendimento (principalmente em trabalhadores com mais 45 anos de idade) e fadiga visual. Os fatores ambientais são normalmente encontrados no setor industrial.

Todos os fatores de riscos ergonômicos são detectados, analisados e corrigidos a partir da AET – Análise Ergonômica do Trabalho. Esse documento é essencial para a avaliação (quantitativa e qualitativa) dos riscos ergonômicos presentes nas máquinas, postos de trabalho e na execução da atividade profissional.

A ergonomia bem aplicada tornará o ambiente de trabalho mais seguro, saudável, eficiente e produtivo."""

class AcidentesScreen(Screen):
    string = """O que é risco de acidente no trabalho?
risco de acidente tipos de riscos
O que é risco de acidente no trabalho?
A princípio, risco de acidentes são todos os fatores que colocam em perigo o trabalhador ou afetam sua integridade física ou moral.

No sentido mais amplo, o risco está associado à probabilidade de ocorrência de um acidente e a intensidade dos danos ou perdas causados por essa ocorrência. Ou seja, é a possibilidade de acontecer algo.

Nesse sentido, eles podem ser muito diversificados e presentes no:

arranjo físico inadequado,
pisos pouco resistentes ou irregulares, material ou matéria-prima fora de especificação,
utilização de máquinas e equipamentos sem proteção,
ferramentas impróprias ou defeituosas,
iluminação excessiva ou insuficiente,
instalações elétricas defeituosas,
probabilidade de incêndio ou explosão,
armazenamento inadequado,
animais peçonhentos e
outras situações de risco que poderão contribuir para a ocorrência de acidentes.
Diferença prática entre risco e perigo no ambiente de trabalho
Perigo e risco são dois termos aparentemente semelhantes, mas que possuem significados diferentes. Sendo assim, nem sempre um perigo é um risco.

Além disso, existem várias definições para perigo no ambiente de trabalho. A mais simples e objetiva é: perigo é tudo aquilo que tem potencial de causar uma perda ou fatalidade.

Nesse sentido, um perigo somente representará um risco quando houver exposição de um funcionário a uma fonte geradora.

Por exemplo, o perigo no ambiente de trabalho pode ser diferenciado por:

Ambientes de trabalho: locais de trabalho muito quentes, frias, empoeiradas, sujas, ruidosas ou escuras, com presença de gases tóxicos, vapores, fumos e etc.
Equipamentos: partes móveis de equipamentos sem dispositivos de proteção e em  condições ruins de uso.
Materiais: substâncias perigosas/tóxicas como, solventes, ácidos, gases, material particulado sólido, entre outros.
Sistema de trabalho: fatores relacionados aos sistemas de trabalho: conteúdo e organização do trabalho, gerenciamento ou cultura organizacional.
Trabalhadores: insuficiência ou falta de capacitação, inexistência de políticas de segurança, fadiga, uso de entorpecentes e álcool, pressão no ambiente de trabalho, assédio moral, carga excessiva de trabalho e etc.
A definição de risco é a probabilidade de algo acontecer em um determinado evento ou local potencialmente perigoso, gerando consequências aos envolvidos. Ou seja, é quando a pessoa é exposta ao perigo.

O nível de risco é estipulado pela combinação da severidade dos possíveis danos e da probabilidade ou chance de sua ocorrência.

A NR9 classifica os riscos em 5 tipos, sendo eles: riscos físicos, químicos, biológicos, ergonômicos e acidentais.

Quais são os fatores de risco de acidente no ambiente de trabalho?
risco de acidente riscos fisicos exemplos
Fatores de risco de acidente no ambiente de trabalho.
Os fatores de risco de acidentes colocam o trabalhador em uma situação vulnerável e que afetem sua integridade e bem-estar físico e psíquico.

Por exemplo, máquinas e equipamentos sem as devidas proteções, ferramentas inapropriadas ou com defeito, falta de iluminação adequada, problemas com a eletricidade, probabilidades de incêndios ou explosões, entre outros.

Manter o local de trabalho seguro e livre de acidentes e ferimentos graves para todos os funcionários começa com a identificação e avaliação dos riscos.

Antes de começar a controlar os riscos, é preciso saber quais são e como interagem com as operações do dia a dia.

Só então você pode começar a trabalhar em maneiras de reduzir, mitigar e eliminar os riscos o máximo possível para tornar o local de trabalho mais seguro para todos.

Tipos de riscos presentes no ambiente de trabalho
risco de acidente riscos quimicos
Tipos de risco de acidente ambiente de trabalho.
São considerados como riscos geradores de acidentes:

Arranjo físico deficiente:

prédios com área insuficiente;
localização imprópria de máquinas e equipamentos;
má arrumação e limpeza;
sinalização incorreta ou inexistente;
pisos desnivelados, obstruídos e/ou irregulares.
Máquinas e equipamentos sem proteção:

Máquinas obsoletas;
máquinas sem proteção em pontos de transmissão e de operação;
comando de liga/desliga fora do alcance do operador;
máquinas e equipamentos com defeitos ou inadequados;
não fornecimento de EPI ou EPI inadequado e/ou vencido.
Ferramentas inadequadas ou defeituosas:

Ferramentas usadas de forma incorreta;
falta de fornecimento de ferramentas adequadas;
falta de manutenção.
Eletricidade:

Instalação elétrica imprópria, com defeito ou exposta;
fios desencapados;
falta de aterramento elétrico;
falta de manutenção.
Incêndio ou explosão:

Armazenamento inadequado de inflamáveis e/ou gases;
manipulação e transporte inadequado de produtos inflamáveis e perigosos;
sobrecarga em rede elétrica;
falta de sinalização;
falta de equipamentos de combate ou equipamentos defeituosos.
Importância da avaliação do risco de acidente no trabalho
As medidas de controle de risco são uma ferramenta crucial para ajudar na prevenção de acidentes ou ferimentos no local de trabalho.

Por isso, elas devem fazer parte do plano mais amplo de saúde e segurança da empresa, fornecendo um método para identificar, controlar e reduzir os riscos presentes no local de trabalho.

Ao serem utilizadas como parte de um plano abrangente de saúde e segurança ocupacional, a avaliação de risco e as medidas de controle fornecem uma série de benefícios ao seu local de trabalho.

Identificação de empregados em situação de risco – Saber quem está em maior risco e a que fatores de risco estão expostos significa que um plano para mitigar ou eliminar esses riscos pode ser desenvolvido.
Consciência dos fatores que não podem ser eliminados – Pode ser possível eliminar completamente alguns dos fatores de risco, entretanto, alguns fatores estarão sempre presentes e só podem ser reduzidos. A conscientização desses fatores significa que os expostos sabem o que procurar e compreender a importância de quaisquer métodos de mitigação.
Determinações de eficiência dos métodos de controle – A reavaliação contínua dos riscos permite determinar se os métodos de controle aplicados foram eficazes para reduzir ou eliminar os riscos ou se eles devem ser reavaliados.
Prevenir ou reduzir os casos de acidentes ou ferimentos – Quando implementados como parte do projeto original do local de trabalho e de seus planos de saúde e segurança, as medidas de controle e avaliações de risco reduzirão ou eliminarão o número de acidentes ou lesões.
Cumprir as obrigações legais – Dependendo da jurisdição e do tipo de negócio e local de trabalho, pode haver obrigações legais que exijam a identificação de riscos e a implementação de medidas de controle em conformidade. O não cumprimento pode resultar em multas."""

class SesmtScreen(Screen): 
    def mudar(self):       
        try:
            g = int(self.ids.g.text)
            n = int(self.ids.t.text)
            dimensionamento.dimensionamento_sesmt(g,n)
            self.ids.error.text = ' '
            self.ids.l.text = dimensionamento.resposta 
        except:
            self.ids.error.text = 'Digite o numero correto!'
        

        
sm.add_widget(SesmtScreen(name='cipa'))
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(PrincipalScreen(name= 'principal'))
sm.add_widget(DimensionamentoScreen(name='dimensionamento'))


class TestApp(MDApp):
    def build(self):        
        kv = Builder.load_file("telas.kv")
        sm = kv
        return sm

    def open_nrs(self):
        url = 'https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/seguranca-e-saude-no-trabalho/ctpp-nrs/normas-regulamentadoras-nrs'
        webbrowser.open(url)

TestApp().run()