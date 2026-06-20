class Partida:
    
    #e: jugador defensor, jugador atacante, facción defensora, facción atacante y mapa
    #s: objeto Partida inicializado
    # Crea una nueva partida con sus jugadores, facciones, mapa y recursos iniciales
    def __init__(
        self,
        jugador_defensor,
        jugador_atacante,
        faccion_defensor,
        faccion_atacante,
        mapa
    ):

        self.jugador_defensor = jugador_defensor
        self.jugador_atacante = jugador_atacante

        self.faccion_defensor = faccion_defensor
        self.faccion_atacante = faccion_atacante

        self.mapa = mapa

        # ====================================
        # ECONOMÍA
        # ====================================

        self.oro_defensor = 1500
        self.oro_atacante = 1500

        self.bono_atacante = 0

        # ====================================
        # RONDAS
        # ====================================

        self.ronda = 1

        self.victorias_defensor = 0
        self.victorias_atacante = 0

        # ====================================
        # FASES
        # ====================================

        self.fase = "DEFENSOR"

        # ====================================
        # ENTIDADES ACTIVAS
        # ====================================

        self.torres = []
        self.muros = []
        self.unidades = []

        self.finalizada = False
        self.ganador = None

    # ==================================================
    # LOOP PRINCIPAL
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Actualiza la partida ejecutando el combate cuando corresponde
    def actualizar(self):

        if self.finalizada:
            return

        if self.fase != "COMBATE":
            return

        self.ejecutar_combate()

    # ==================================================
    # COMPRAS
    # ==================================================

    #e: torre, fila y columna
    #s: valor booleano
    # Coloca una torre en el mapa si cumple las condiciones
    def colocar_torre(self, torre, fila, columna):

        if self.fase != "DEFENSOR":
            return False

        if self.oro_defensor < torre.costo:
            return False

        if self.mapa.colocar(fila, columna, torre):

            self.torres.append(torre)
            self.oro_defensor -= torre.costo

            return True

        return False

    #e: muro, fila y columna
    #s: valor booleano
    # Coloca un muro en el mapa si cumple las condiciones
    def colocar_muro(self, muro, fila, columna):

        if self.fase != "DEFENSOR":
            return False

        if self.oro_defensor < muro.costo:
            return False

        if self.mapa.colocar(fila, columna, muro):

            self.muros.append(muro)
            self.oro_defensor -= muro.costo

            return True

        return False

    #e: unidad, fila y columna
    #s: valor booleano
    # Coloca una unidad atacante en el mapa
    def colocar_unidad(self, unidad, fila, columna):

        if self.fase != "ATAQUE":
            return False

        if self.oro_atacante < unidad.costo:
            return False

        if self.mapa.colocar(fila, columna, unidad):

            self.unidades.append(unidad)
            self.oro_atacante -= unidad.costo

            return True

        return False

    # ==================================================
    # CAMBIO DE FASE
    # ==================================================

    #e: ninguna
    #s: valor booleano
    # Cambia la fase actual de la partida
    def pasar_fase(self):

        # El jugador decide avanzar de fase; el oro restante no debe
        # impedir el avance, solo se informa para que decida si seguir comprando.
        if self.fase == "DEFENSOR":

            self.fase = "ATAQUE"
            return True

        elif self.fase == "ATAQUE":

            self.fase = "COMBATE"
            return True

        return False

    # ==================================================
    # COMBATE
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Ejecuta las acciones principales del combate
    def ejecutar_combate(self):

        self.mover_unidades()

        self.torres_atacan()

        self.limpiar_muertos()

        self.verificar_fin_ronda()

    # ==================================================
    # MOVIMIENTO
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Mueve las unidades atacantes y aplica daño cuando corresponde
    def mover_unidades(self):

        for unidad in list(self.unidades):

            if not unidad.esta_viva():
                continue

            for _ in range(unidad.velocidad):

                # Si la unidad ya esta junto a la base, se queda fija
                # atacandola cada turno hasta morir o hasta destruirla.
                if self.adyacente_a_base(unidad.fila, unidad.columna):
                    self.mapa.base.recibir_dano(unidad.dano)
                    self.bono_atacante += unidad.dano
                    break

                fila = unidad.fila
                columna = unidad.columna

                destino_fila = fila
                destino_columna = columna

                if fila < self.mapa.base.fila:
                    destino_fila += 1
                elif fila > self.mapa.base.fila:
                    destino_fila -= 1

                if columna < self.mapa.base.columna:
                    destino_columna += 1
                elif columna > self.mapa.base.columna:
                    destino_columna -= 1

                # Llego a la base: ataca pero permanece en el mapa
                if (
                    destino_fila == self.mapa.base.fila and
                    destino_columna == self.mapa.base.columna
                ):

                    self.mapa.base.recibir_dano(unidad.dano)

                    self.bono_atacante += unidad.dano

                    break

                objeto = self.mapa.obtener_objeto(
                    destino_fila,
                    destino_columna
                )

                if objeto is None:

                    self.mapa.mover_unidad(
                        unidad,
                        destino_fila,
                        destino_columna
                    )

                elif hasattr(objeto, "velocidad"):

                    # Es otra unidad atacante (aliada), no un obstaculo
                    # del defensor: simplemente espera a que se libere
                    # la celda, sin causarle daño.
                    break

                else:

                    if hasattr(objeto, "recibir_dano"):

                        objeto.recibir_dano(unidad.dano)

                        self.bono_atacante += unidad.dano

                    break

    #e: fila y columna
    #s: valor booleano
    # Verifica si una posición está junto a la base
    def adyacente_a_base(self, fila, columna):

        distancia = max(
            abs(fila - self.mapa.base.fila),
            abs(columna - self.mapa.base.columna)
        )

        return distancia <= 1 and not (
            fila == self.mapa.base.fila and
            columna == self.mapa.base.columna
        )

    # ==================================================
    # TORRES
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Hace que las torres ataquen a las unidades enemigas
    def torres_atacan(self):

        for torre in self.torres:

            if not torre.esta_viva():
                continue

            torre.intentar_habilidad(self.mapa)

            objetivo = self.mapa.unidad_mas_cercana(
                torre.fila,
                torre.columna,
                torre.alcance
            )

            if objetivo:
                torre.atacar(objetivo)

    # ==================================================
    # LIMPIEZA
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Elimina del mapa las entidades destruidas
    def limpiar_muertos(self):

        for unidad in list(self.unidades):

            if not unidad.esta_viva():

                self.mapa.eliminar(
                    unidad.fila,
                    unidad.columna
                )

                self.unidades.remove(unidad)

                self.oro_defensor += 25

        for torre in list(self.torres):

            if not torre.esta_viva():

                self.mapa.eliminar(
                    torre.fila,
                    torre.columna
                )

                self.torres.remove(torre)

        for muro in list(self.muros):

            if muro.esta_destruido():

                self.mapa.eliminar(
                    muro.fila,
                    muro.columna
                )

                self.muros.remove(muro)

    # ==================================================
    # RONDAS
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Verifica si la ronda actual ha terminado
    def verificar_fin_ronda(self):

        # atacante gana: la base fue destruida

        if self.mapa.base.esta_destruida():

            self.victorias_atacante += 1

            self.reiniciar_ronda()

            return

        # defensor gana: ya estamos en fase de combate (no se puede comprar
        # mas) y no quedan unidades atacantes con vida en el campo

        unidades_vivas = [u for u in self.unidades if u.esta_viva()]

        if len(unidades_vivas) == 0:

            self.victorias_defensor += 1

            self.reiniciar_ronda()

            return

    # ==================================================
    # NUEVA RONDA
    # ==================================================

    #e: ninguna
    #s: ninguna
    # Reinicia la ronda o finaliza la partida si alguien alcanzó tres victorias
    def reiniciar_ronda(self):

        if self.victorias_defensor >= 3:

            self.finalizada = True
            self.ganador = self.jugador_defensor

            self.jugador_defensor.sumar_victoria_defensor()

            return

        if self.victorias_atacante >= 3:

            self.finalizada = True
            self.ganador = self.jugador_atacante

            self.jugador_atacante.sumar_victoria_atacante()

            return

        self.ronda += 1

        self.oro_defensor += 500

        self.oro_atacante += 500
        self.oro_atacante += self.bono_atacante

        self.bono_atacante = 0

        self.torres.clear()
        self.muros.clear()
        self.unidades.clear()

        self.mapa.reiniciar()

        self.fase = "DEFENSOR"