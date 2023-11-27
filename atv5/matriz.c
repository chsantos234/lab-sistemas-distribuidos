#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

// mpicc matriz.c -o matriz && mpirun -np 4 ./matriz

int main(int argc, char** argv){
    // inicializar
    MPI_Init(NULL, NULL);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // ordem da matriz
    int m_order = 100;
    int block_per_process = m_order * m_order / world_size;

    int A[m_order][m_order];
    int B[m_order][m_order];
    int C[m_order][m_order];

    if(world_size != 4){
        fprintf(stderr, "Número de processos deve ser igual a 4 para %s\n", argv[0]);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    for (int i = 0; i < m_order; i++){
        for (int j = 0; j < m_order; j++){
            A[i][j] = 2;
            B[i][j] = 3;
            C[i][j] = 0;
        }
    }
    // upper left
    if(world_rank == 0){
        for (int i = 0; i < m_order / 2; i++){
            for (int j = 0; j < m_order / 2; j++){
                C[i][j] = A[i][j] + B[i][j];
            }
        }

        for(int i = 0; i < m_order / 2; i++){
            for(int j = m_order / 2; j < m_order; j++){
                MPI_Recv(&C[i][j], 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
        }
        for (int i = m_order / 2; i < m_order; i++){
            for(int j = 0; j < m_order / 2; j++){
                MPI_Recv(&C[i][j], 1, MPI_INT, 2, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
        }
        for(int i = m_order / 2; i < m_order; i++){
            for(int j = m_order / 2; j < m_order; j++){
                MPI_Recv(&C[i][j], 1, MPI_INT, 3, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
        }

    }
    // upper right
    if(world_rank == 1){
        for(int i = 0; i < m_order / 2; i++){
            for(int j = m_order / 2; j < m_order; j++){
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        for (int i = 0; i < m_order / 2; i++){
            for (int j = m_order / 2; j < m_order; j++){
                MPI_Send(&C[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
            }
        }
    }
    // lower left
    if(world_rank == 2){
        for (int i = m_order / 2; i < m_order; i++){
            for(int j = 0; j < m_order / 2; j++){
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        for (int i = m_order / 2; i < m_order; i++){
            for(int j = 0; j < m_order / 2; j++){
                MPI_Send(&C[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
            }
        }
    }
    // lower right
    if(world_rank == 3){
        for(int i = m_order / 2; i < m_order; i++){
            for(int j = m_order / 2; j < m_order; j++){
                C[i][j] = A[i][j] + B[i][j];
                MPI_Send(&C[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
            }
        }
        for(int i = m_order / 2; i < m_order; i++){
            for(int j = m_order / 2; j < m_order; j++){
                MPI_Send(&C[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
            }
        }
    }
    if(world_rank == 0){
        for (int i = 0; i < m_order; i++){
            for (int j = 0; j < m_order; j++){
                printf("%d ", C[i][j]);
            }
            printf("\n");
        }
    }
    MPI_Finalize();
}